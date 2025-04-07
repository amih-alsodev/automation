import ast
import json
import pytest
from datetime import datetime
from playwright.sync_api import Playwright

from utilities.api.api_product_req import APIProduct
from utilities.data_processing import DataProcessing


def test_create_product_with_full_data(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_full_data"))

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))


def test_create_product_with_only_req_data(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_only_req_data"))

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    product_data = response_body[0]
    product_id = product_data["id"]
    response = api_product.delete_product_by_id(playwright, product_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"


def test_create_product_with_empty_data(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    json_data = data_processing.get_value_by_key(payloads_list, "create_product_with_empty_data")

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))
    expected_result = {
        "price": ["Это поле обязательно."],
        "group_product_id": ["Это поле обязательно."],
        "specifications": ["Это поле обязательно."],
        "category": ["Это поле обязательно."],
        "name_ro": ["Это поле обязательно."]
    }
    json_str_1 = json.dumps(expected_result, sort_keys=True)
    json_str_2 = json.dumps(response_body[0], sort_keys=True)
    assert json_str_1 == json_str_2, f"JSON objects are different:\n{json_str_1}\n{json_str_2}"


def test_get_products_list(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_list(playwright, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))


def test_get_product_with_id(playwright: Playwright):
    # 197
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))


@pytest.mark.smoke
def test_update_product_price(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["price"] = "1500"
    response_body_list = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, response_body_list, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    actual_product_price = response_body[0]["price"]
    assert actual_product_price == "1500.00"


@pytest.mark.smoke
def test_update_product_quantity(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_only_req_data"))

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    product_data = response_body[0]
    product_id = product_data["id"]

    response = api_product.get_product_by_id(playwright, product_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["qty"] = 15
    response_body_list = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, response_body_list, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    actual_product_qty = response_body[0]["qty"]
    assert actual_product_qty == 15

    response = api_product.delete_product_by_id(playwright, product_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"


@pytest.mark.smoke
def test_update_product_old_price(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_only_req_data"))

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    product_data = response_body[0]
    product_id = product_data["id"]

    response = api_product.get_product_by_id(playwright, product_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["old_price"] = "7001"
    response_body_list = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, response_body_list, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    actual_old_price = response_body[0]["old_price"]
    assert actual_old_price == "7001.00"

    response = api_product.delete_product_by_id(playwright, product_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

@pytest.mark.smoke
def test_update_product_old_price_empty(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["old_price"] = None
    response_body_list = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, response_body_list, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    actual_old_price = response_body[0]["old_price"]
    assert actual_old_price is None


@pytest.mark.smoke
def test_update_product_specifications_to_have_data(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_full_data"))

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()

    response_body["specifications"] = json_data[0]["specifications"]
    response_body_list = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, response_body_list, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    json_str_1 = json.dumps(json_data[0]["specifications"], sort_keys=True)
    json_str_2 = json.dumps(response_body[0]["specifications"], sort_keys=True)
    assert json_str_1 == json_str_2, f"JSON objects are different:\n{json_str_1}\n{json_str_2}"


@pytest.mark.smoke
def test_update_product_specifications_to_be_empty(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    specification_data = []
    response_body["specifications"] = specification_data
    json_data = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    json_str_1 = json.dumps(specification_data, sort_keys=True)
    json_str_2 = json.dumps(response_body[0]["specifications"], sort_keys=True)
    assert json_str_1 == json_str_2, f"JSON objects are different:\n{json_str_1}\n{json_str_2}"


@pytest.mark.smoke
def test_update_product_names(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name_ro = response_body["name_ro"]
    name_ru = response_body["name_ru"]
    name_en = response_body["name_en"]
    name_uk = response_body["name_uk"]
    updated_name_ro = f"{name_ro}_{timestamp}"
    updated_name_ru = f"{name_ru}_{timestamp}"
    updated_name_en = f"{name_en}_{timestamp}"
    updated_name_uk = f"{name_uk}_{timestamp}"
    response_body["name_ro"] = updated_name_ro
    response_body["name_ru"] = updated_name_ru
    response_body["name_en"] = updated_name_en
    response_body["name_uk"] = updated_name_uk
    json_data = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    assert response_body[0]["name_ro"] == updated_name_ro
    assert response_body[0]["name_ru"] == updated_name_ru
    assert response_body[0]["name_en"] == updated_name_en
    assert response_body[0]["name_uk"] == updated_name_uk


@pytest.mark.smoke
def test_update_product_category(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    category_id = [2970]
    response_body["category"] = category_id
    json_data = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    json_str_1 = json.dumps(category_id, sort_keys=True)
    json_str_2 = json.dumps(response_body[0]["category"], sort_keys=True)
    assert json_str_1 == json_str_2, f"JSON objects are different:\n{json_str_1}\n{json_str_2}"


@pytest.mark.smoke
def test_update_product_all_fields(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_full_data"))

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    assert response_body[0]["bookmark"] == ast.literal_eval(json_data[0]["bookmark"])
    assert response_body[0]["price"] == json_data[0]["price"]
    assert response_body[0]["qty"] == json_data[0]["qty"]
    assert response_body[0]["sort_priority"] == json_data[0]["sort_priority"]
    assert response_body[0]["old_price"] == json_data[0]["old_price"]
    assert response_body[0]["group_product_id"] == json_data[0]["group_product_id"]
    assert int(float(response_body[0]["weight"])) == json_data[0]["weight"]
    assert int(float(response_body[0]["height"])) == json_data[0]["height"]
    assert int(float(response_body[0]["width"])) == json_data[0]["width"]
    assert int(float(response_body[0]["length"])) == json_data[0]["length"]
    assert response_body[0]["brand_id"] == ast.literal_eval(json_data[0]["brand_id"])
    assert response_body[0]["keywords"] == json_data[0]["keywords"]
    assert response_body[0]["name_ro"] == json_data[0]["name_ro"]
    assert response_body[0]["name_ru"] == json_data[0]["name_ru"]
    assert response_body[0]["name_en"] == json_data[0]["name_en"]
    assert response_body[0]["name_uk"] == json_data[0]["name_uk"]
    assert response_body[0]["short_description_ro"] == json_data[0]["short_description_ro"]
    assert response_body[0]["short_description_ru"] == json_data[0]["short_description_ru"]
    assert response_body[0]["short_description_en"] == json_data[0]["short_description_en"]
    assert response_body[0]["short_description_uk"] == json_data[0]["short_description_uk"]
    assert response_body[0]["description_ro"] == json_data[0]["description_ro"]
    assert response_body[0]["description_ru"] == json_data[0]["description_ru"]
    assert response_body[0]["description_en"] == json_data[0]["description_en"]
    assert response_body[0]["description_uk"] == json_data[0]["description_uk"]
    assert response_body[0]["unit_measurement_ro"] == json_data[0]["unit_measurement_ro"]
    assert response_body[0]["unit_measurement_ru"] == json_data[0]["unit_measurement_ru"]
    assert response_body[0]["unit_measurement_en"] == json_data[0]["unit_measurement_en"]
    assert response_body[0]["unit_measurement_uk"] == json_data[0]["unit_measurement_uk"]
    assert response_body[0]["seo_title_ro"] == json_data[0]["seo_title_ro"]
    assert response_body[0]["seo_title_ru"] == json_data[0]["seo_title_ru"]
    assert response_body[0]["seo_title_en"] == json_data[0]["seo_title_en"]
    assert response_body[0]["seo_title_uk"] == json_data[0]["seo_title_uk"]
    assert response_body[0]["seo_description_ro"] == json_data[0]["seo_description_ro"]
    assert response_body[0]["seo_description_ru"] == json_data[0]["seo_description_ru"]
    assert response_body[0]["seo_description_en"] == json_data[0]["seo_description_en"]
    assert response_body[0]["seo_description_uk"] == json_data[0]["seo_description_uk"]
    assert response_body[0]["seo_keywords_ro"] == json_data[0]["seo_keywords_ro"]
    assert response_body[0]["seo_keywords_ru"] == json_data[0]["seo_keywords_ru"]
    assert response_body[0]["seo_keywords_en"] == json_data[0]["seo_keywords_en"]
    assert response_body[0]["seo_keywords_uk"] == json_data[0]["seo_keywords_uk"]
    assert response_body[0]["code"] == json_data[0]["code"]


def test_update_product_brand(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132812", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["brand_id"] = "12833"
    json_data = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    product_data = response.json()[0]
    assert product_data["brand_id"] == "12833"


def test_update_product_with_old_price_null(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()
    json_data = []

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data.append(data_processing.get_value_by_key(payloads_list, "create_product_with_only_req_data"))

    response = api_product.create_product(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body[0]["price"] = 1532

    response = api_product.update_one_key_of_product_with_id(playwright, response_body, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    product_data = response.json()[0]
    assert product_data["price"] == "1532.00"


def test_update_product_with_group_id_null(playwright: Playwright):
    data_processing = DataProcessing()
    api_product = APIProduct()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    response = api_product.get_product_by_id(playwright, "132828", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body["price"] = 1533
    json_data = [response_body]

    response = api_product.update_one_key_of_product_with_id(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    product_data = response.json()[0]
    assert product_data["price"] == "1533.00"
