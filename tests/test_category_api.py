import json
from datetime import datetime

from utilities.api.api_category_req import APICategory
from utilities.data_processing import DataProcessing


def test_create_category(playwright):
    data_processing = DataProcessing()
    api_category = APICategory()

    sites_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(sites_list, "jbl")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    payload = data_processing.get_value_by_key(payloads_list, "create_category_with_data")

    response = api_category.create_category(playwright, payload, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response_body = response.json()
    category_id = response_body[0]["id"]

    response = api_category.delete_category_by_id(playwright, category_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response = api_category.get_category_details_by_id(playwright, category_id, site_token, api_token)
    assert response.json()["detail"] == "Не найдено."


def test_create_category_with_empty_data(playwright):
    data_processing = DataProcessing()
    api_category = APICategory()

    sites_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(sites_list, "used.md")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data = payloads_list[0]["category"][0]["create_category_with_empty_data"]

    response = api_category.create_category(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    print(json.dumps(response_body, indent=4, ensure_ascii=False))


def test_create_two_categories(playwright):
    data_processing = DataProcessing()
    api_category = APICategory()

    sites_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_data = data_processing.get_value_by_key(sites_list, "used.md")
    site_token = site_data["token"]
    api_token = site_data["external_API_token"]

    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    json_data = payloads_list[0]["category"][0]["create_two_categories"]

    response = api_category.create_category(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    category_one_id = response_body[0]["id"]
    category_two_id = response_body[1]["id"]

    response = api_category.get_category_details_by_id(playwright, category_one_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response = api_category.get_category_details_by_id(playwright, category_two_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response = api_category.delete_category_by_id(playwright, category_one_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response = api_category.delete_category_by_id(playwright, category_two_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"


def test_update_created_category(playwright):
    data_processing = DataProcessing()
    api_category = APICategory()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    payloads_list = data_processing.get_list_from_file("api_req_payloads.json", "payloads")
    site_token = site_credentials_list[0]["token"]
    api_token = site_credentials_list[0]["external_API_token"]
    json_data = payloads_list[0]["category"][0]["create_category_with_data"]

    response = api_category.create_category(playwright, json_data, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()
    response_body[0]["name_ro"] = "test update created category name"
    category_id = response_body[0]["id"]
    response = api_category.update_one_key_of_category_with_id(playwright, category_id, response_body[0], site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response = api_category.get_category_details_by_id(playwright, category_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()

    assert response_body["name_ro"] == "test update created category name"

    response = api_category.delete_category_by_id(playwright, category_id, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"


def test_update_existed_category(playwright):
    data_processing = DataProcessing()
    api_category = APICategory()

    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")
    site_token = site_credentials_list[0]["token"]
    api_token = site_credentials_list[0]["external_API_token"]
    response = api_category.get_category_details_by_id(playwright, "2970", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name_ro = response_body["name_ro"]
    updated_name_ro = f"{name_ro}_{timestamp}"
    response_body["name_ro"] = updated_name_ro

    response = api_category.update_one_key_of_category_with_id(playwright, "2970", response_body, site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response = api_category.get_category_details_by_id(playwright, "2970", site_token, api_token)
    assert response.ok, f"API request failed with status {response.status}: {response.text()}"
    response_body = response.json()

    assert response_body["name_ro"] == updated_name_ro



