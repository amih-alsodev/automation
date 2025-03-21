import json

import jsonschema
from playwright.sync_api import Playwright

from utilities.api.api_general_req import APIGeneral
from utilities.api.api_order import APIOrder
from utilities.data_processing import DataProcessing


def test_create_cart_order_payment_paypal_req_fields(playwright: Playwright):
    data_processing = DataProcessing()
    with_api_order = APIOrder()

    sites_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(sites_list, "habsev.md")
    site_token = site_data["token"]

    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    payload = data_processing.get_value_by_key(payloads_list, "cart_paypal_req_fields")
    print(payload)

    schemes_list = data_processing.get_list_from_file("response_schemes.json", "schemes")
    cart_schemes_list = data_processing.get_value_by_key(schemes_list, "cart")
    scheme_paypal_payment = data_processing.get_value_by_key(cart_schemes_list, "paypal")

    response = with_api_order.create_cart_order(playwright, payload, site_token)

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))
    assert jsonschema.validate(instance=response_body, schema=scheme_paypal_payment) is None


def test_create_cart_order_with_tax(playwright: Playwright):
    data_processing = DataProcessing()
    with_api_order = APIOrder()
    with_api_general = APIGeneral()

    sites_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(sites_list, "habsev.md")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    payload = data_processing.get_value_by_key(payloads_list, "cart_tax_req_fields")

    response = with_api_order.create_cart_order(playwright, payload, site_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    order_id = response_body["order_id"]

    response = with_api_general.get_order_data(playwright, order_id, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))

