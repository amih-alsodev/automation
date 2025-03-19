from playwright.sync_api import Page


class CartPage:
    """
    Represents the cart element or page, depends on the type selected in global settings, with its functionality
    """

    def __init__(self, page: Page):
        """Initialize locators for cart elements"""
        self.page = page
        self.view_one_step_one_close_button = page.locator('#close-cart')
        self.view_one_step_one_product_cards_list = page.locator('.cart__items-container .cart__items')
        self.view_one_step_one_product_card_title = page.locator('.product__head .product__name')
        self.view_one_step_one_product_card_delete_button = page.locator('.product__info .btn__delete')
        self.view_one_step_one_product_card_counter_minus_button = page.locator('[data-action="minus"]')
        self.view_one_step_one_product_card_counter_minus_button = page.locator('[data-action="plus"]')
        self.view_one_step_one_submit_an_application_button = page.locator('#cart-request')
        self.view_one_step_two_close_button = page.locator('.head .btn__close')
        # Change the locator for view_one_step_two_name_input when the testing attribute will be added
        self.view_one_step_two_name_input = page.locator('.personal__date .form__item:nth-of-type(1) input')
        # Change the locator for view_one_step_two_email_input when the testing attribute will be added
        self.view_one_step_two_email_input = page.locator('.personal__date .form__item:nth-of-type(3) input')
        self.view_one_step_two_agree_checkbox = page.locator('#term')
        self.view_one_step_two_payment_type_cash_radio_button = page.locator('#cash')
        self.view_one_step_two_payment_type_card_radio_button = page.locator('#card')
        self.view_one_step_two_payment_type_paynet_radio_button = page.locator('#paynet')
        self.view_one_step_two_payment_type_bpay_radio_button = page.locator('#bpay')
        self.view_one_step_two_payment_type_bpay_qr_radio_button = page.locator('#bpay_qr')
        self.view_one_step_two_payment_type_stripe_radio_button = page.locator('#stripe')
        self.view_one_step_two_payment_type_paypal_radio_button = page.locator('#paypal')
        self.view_one_step_two_payment_type_liqpay_radio_button = page.locator('#liqpay')
        self.view_one_step_two_payment_type_card_on_receipt_radio_button = page.locator('#card_on_receipt')
        self.view_one_step_two_delivery_type_delivery_radio_button = page.locator('#delivery')
        # Change the locator for view_one_step_two_region_dropdown when the testing attribute will be added
        self.view_one_step_two_region_dropdown = page.locator(
            '.payment .input__item:nth-of-type(1) .g-select-search.g-select-search--no-label')
        # Change the locator for view_one_step_two_locality_dropdown when the testing attribute will be added
        self.view_one_step_two_locality_dropdown = page.locator(
            '.payment .input__item:nth-of-type(2) .g-select-search.g-select-search--no-label')
        # Change the locator for view_one_step_two_shipping_address_input when the testing attribute will be added
        self.view_one_step_two_shipping_address_input = page.locator('.payment .form__item input')
        # Change the locator for view_one_step_two_comment_input when the testing attribute will be added
        self.view_one_step_two_comment_input = page.locator('.payment .form__item input')
        # Change the locator for view_one_step_two_promocode_input when the testing attribute will be added
        self.view_one_step_two_promocode_input = page.locator('.checkout__items.promocode input')
        self.view_one_step_two_promocode_accept_button = page.locator('.form__button.request')
        self.view_one_step_two_continue_shopping_button = page.locator('.btn.btn__secondary.cart')
        self.view_one_step_two_create_order_button = page.locator('#cart-request')
        self.view_two_clear_cart_button = page.locator('.cart-products .cart-products__header__clear-btn')
        self.view_two_product_cards_list = page.locator('.cart-products .cart-products__items')
        self.view_type_two_product_card_delete_button = page.locator(
            '.plank-card__btns__decrease.ui-action-btn.--dark.--only-icon.--size-small.--fit-content.plank'
            '-card__btns__decrease.delete')
        self.view_two_product_card_plus_button = page.locator(
            '.plank-card__btns__increase.ui-action-btn.--dark.--only-icon.--size-small.--fit-content')
