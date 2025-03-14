from playwright.sync_api import Page

from pageObjects.auth_pop_up import AuthPopUp
from utilities.data_processing import DataProcessing


class HeaderElement:
    """Represents the header element with its functionality"""

    def __init__(self, page: Page):
        """Initialize locators for header elements"""
        self.page = page
        self.menu_button = page.locator('#menuBtn')
        self.view_one_search_input = page.locator('.search__input')
        self.view_one_compare_button = page.locator('.btn__action.compare__btn.compare__link')
        self.view_one_favorite_button = page.locator('.btn__action.favorite__link.favorite__btn')
        self.cart_button = page.locator('.btn__action.btn__cart')
        self.log_in_button = page.locator('.btn__action.btn__auth')
        self.view_two_search_button = page.locator('#search')
        self.view_two_favorite_button = page.locator('.btn__action.favorite__link')
        self.view_two_compare_button = page.locator('.btn__action.compare__btn')
        self.view_three_menu_button = page.locator('.header-tertiary__catalog-btn')
        self.view_three_compare_button = page.locator('.header-tertiary__icon.header-tertiary__icon--compare')
        self.view_three_favorite_button = page.locator('header-tertiary__icon header-tertiary__icon--favourite')
        self.view_three_cart_button = page.locator('.header-tertiary__icon.header-tertiary__icon--cart')
        self.view_three_lang_dropdown = page.locator('.header-tertiary__lang')
        self.view_four_search_button = page.locator('#casa-open-search-button')
        self.view_four_cart_button = page.locator('.header-casa__actions-btn.header-casa__actions-btn--cart')
        self.view_four_favorite_button = page.locator('.header-casa__actions-btn.header-casa__actions-btn--favorites')
        self.view_four_compare_button = page.locator('.header-casa__actions-btn.header-casa__actions-btn--compare')
        self.view_four_log_in_button = page.locator('.header-casa__actions-btn.header-casa__actions-btn--auth')
        self.view_four_lang_dropdown = page.locator('.language-switch__button')

    def open_login_popup(self, view_type: str):
        """
        Open login pop up by clicking log in/cabinet button.

        :param view_type: Type of header which is selected in site global setting.
        :return: An instance of the AuthPopUp class, which represents the login popup.
        """
        data_processing = DataProcessing()
        elements_list = data_processing.get_list_from_file("element_types.json", "elements")
        if view_type == data_processing.get_value_by_key(elements_list, "view_1"):
            self.view_three_menu_button.click()
        else:
            self.log_in_button.click()

        auth_pop_up = AuthPopUp(self.page)
        return auth_pop_up
