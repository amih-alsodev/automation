import jsonschema
from playwright.sync_api import Playwright
from utilities.api.api_specification_req import APISpecification
from utilities.data_processing import DataProcessing


def test_create_specification(playwright: Playwright):
    data_processing = DataProcessing()
    api_specification = APISpecification()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data = data_processing.get_value_by_key(payloads_list, "create_specification_with_data")
    schemes_list = data_processing.get_list_from_file("response_schemes.json", "schemes")
    specification_scheme = data_processing.get_value_by_key(schemes_list, "specification")

    response = api_specification.create_specification(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    specification_data = response_body[0]
    specification_id = specification_data["id"]

    assert jsonschema.validate(instance=response_body, schema=specification_scheme) is None
    assert specification_data["name_ro"] == json_data[0]["name_ro"]
    assert specification_data["name_ru"] == json_data[0]["name_ru"]
    assert specification_data["name_en"] == json_data[0]["name_en"]
    assert specification_data["name_uk"] == json_data[0]["name_uk"]

    response = api_specification.delete_specification_by_id(playwright, specification_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"


def test_get_specification_list(playwright: Playwright):
    data_processing = DataProcessing()
    api_specification = APISpecification()

    # site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    # site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    # site_token = site_data["token"]
    # api_token = site_data["external_API_token"]
    # payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    # json_data = data_processing.get_value_by_key(payloads_list, "create_specification_with_data")
    # schemes_list = data_processing.get_list_from_file("response_schemes.json", "schemes")
    # specification_scheme = data_processing.get_value_by_key(schemes_list, "specification")
    #
    # response = api_specification.get_specifications_list(playwright, site_token, api_token)


