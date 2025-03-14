from playwright.sync_api import Page

from utilities.data_processing import DataProcessing


class AuthPopUp:
    """Represents the authentication popup with login functionality."""

    def __init__(self, page: Page):
        """Initialize locators for authentication popup elements."""
        self.page = page
        self.close_button = page.locator('.btn__close')
        self.email_input = page.locator('.form__item > input[type="text"]')
        self.password_input = page.locator('input[type="password"]')
        self.log_in_button = page.locator('.request')

    def login_with_user_credentials(self):
        """
        Reads user credentials from a JSON file and performs user authentication.
        """
        data_processing = DataProcessing()

        users_list = data_processing.get_list_from_file("user_credentials.json", "users")
        user_email = users_list[0]["email"]
        user_password = users_list[0]["password"]

        self.email_input.fill(user_email)
        self.password_input.fill(user_password)
        self.log_in_button.click()
