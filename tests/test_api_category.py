from utils.api.api_category import delete_category_by_id, create_category
from utils.data_processing import get_list_from_file


def test_create_category(playwright):
    site_credentials_list = get_list_from_file("site_credentials.json", "sites")
    payloads_list = get_list_from_file("api_req_payloads.json", "payloads")
    json_data = payloads_list[0]["category"][0]["create_category_with_data"]
    category_id = create_category(playwright, json_data, site_credentials_list[0]["token"], site_credentials_list[0]["external_API_token"])[0]["id"]
    delete_category_by_id(playwright, category_id, site_credentials_list[0]["token"], site_credentials_list[0]["external_API_token"])
