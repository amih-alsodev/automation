import json

import jsonschema
from playwright.sync_api import Playwright

from utilities.api.api_order import APIOrder
from utilities.data_processing import DataProcessing


def test_create_cart_order_payment_paypal_req_fields(playwright: Playwright):
    data_processing = DataProcessing()
    with_api_order = APIOrder()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    schemes_list = data_processing.get_list_from_file("response_schemes.json", "schemes")
    site_data = data_processing.get_credentials_of_site(site_credentials_list, "habsev.md")
    site_token = site_data["token"]

    json_data = payloads_list[0]["order"][0]["cart"][0]["cart_paypal_req_fields"]
    order_scheme = schemes_list[0]["cart"][0]["paypal"]

    response = with_api_order.create_cart_order(playwright, json_data, site_token)

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))
    assert jsonschema.validate(instance=response_body, schema=order_scheme) is None

