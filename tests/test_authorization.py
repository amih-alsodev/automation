from pageObjects.header_element import HeaderElement
from utilities.api.api_general_req import APIGeneral
from playwright.sync_api import expect
from utilities.data_processing import DataProcessing


def test_smth(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_general = APIGeneral()
    data_processing = DataProcessing()
    site_credentials_list = data_processing.get_list_from_file("site_credentials.json", "sites")

    site_data = data_processing.get_value_by_key(site_credentials_list, "jbl")
    site_token = site_data["token"]

    response = api_general.get_global_site_settings(playwright, site_token)
    response_body = response.json()
    header_type = data_processing.get_value_by_key(response_body, "mainNavigationType")

    page.goto("https://stage.ecom.md/ru")
    page.wait_for_function("() => !document.body.hasAttribute('data-n-head')", timeout=5000)
    on_header = HeaderElement(page)
    on_auth_pop_up = on_header.open_login_popup(header_type)
    on_auth_pop_up.login_with_user_credentials()
    expect(on_header.log_in_button).to_contain_text("Cabinet")
