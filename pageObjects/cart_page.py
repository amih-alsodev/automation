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
        # Change the locator for view_two_product_card_minus_button when the testing attribute will be added
        self.view_two_product_card_minus_button = page.locator(
            '.plank-card__btns__decrease.ui-action-btn.--dark.--only-icon.--size-small.--fit-content.plank'
            '-card__btns__decrease')
        # Change the locator for view_two_name_input when the testing attribute will be added
        self.view_two_name_input = page.locator('[data-fetch-key="MyInput:0"] input')
        self.view_two_email_input = page.locator('.ui-input__field [type="email"]')
        # Change the locator for view_two_delivery_type_pickup when the testing attribute will be added
        self.view_two_delivery_type_pickup = page.locator('')
        # Change the locator for view_two_delivery_type_address when the testing attribute will be added
        self.view_two_delivery_type_address = page.locator('')
        self.view_two_delivery_type_address_region_dropdown_menu = page.locator('#vs1__combobox')
        self.view_two_delivery_type_address_region_dropdown_list = page.locator('#vs1__listbox')
        self.view_two_delivery_type_address_locality_dropdown_menu_status_disable = page.locator(
            '.order-form__content__segment__content__inputs .ui-select.--gray.disabled.focus')
        self.view_two_delivery_type_address_locality_dropdown_menu = page.locator('#vs2__combobox')
        self.view_two_delivery_type_address_locality_dropdown_list = page.locator('#vs2__listbox')
        # Change the locator for view_two_promocode_input when the testing attribute will be added
        self.view_two_promocode_input = page.locator('[data-fetch-key="MyInput:3"] input')
        # Change the locator for view_two_comment_input when the testing attribute will be added
        self.view_two_comment_input = page.locator('[data-fetch-key="MyInput:4"] input')
        self.view_two_agree_checkbox = page.locator('.ui-checkbox .ui-checkbox__area')
        self.view_two_create_order_button = page.locator('[type="submit"]')
        self.view_four_product_list_tab = page.locator('#cart-tab')
        self.view_four_personal_data_tab = page.locator('#personal-info-tab')
        self.view_four_delivery_tab = page.locator('#delivery-tab')
        self.view_four_payment_tab = page.locator('#pay-tab')
        self.view_four_product_card_delete_button = page.locator('.product__info .btn__delete')
        self.view_four_product_card_minus_button_status_disabled = page.locator(
            '.product__footer .item__control.minus.disabled')
        self.view_four_product_card_minus_button = page.locator('.product__footer .item__control.minus')
        self.view_four_product_card_plus_button = page.locator('.product__footer .item__control.plus')
        self.view_four_agree_checkbox = page.locator('#term')
        self.view_four_continue_button = page.locator('.summary-sidebar__action .request')
        
        self.view_four_email_input = page.locator('.personal-information-step [type="email"]')
