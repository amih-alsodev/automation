from playwright.sync_api import Playwright


class APIOrder:

    def create_quick_order(self, playwright: Playwright, payload: dict, site_token: str):
        """
        Performs an API request to create quick order.

        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :param site_token: Identifier specifying which site will be loaded
        :return: JSON response containing info about order.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.post(
            "/general/v3/quick-order/",
            data=payload,
            headers={
                "token": site_token,
                "Content-Type": "application/json"
            }
        )

        return response


    def create_cart_order(self, playwright: Playwright, payload: dict, site_token: str):
        """
        Performs an API request to create quick order.

        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :param site_token: Identifier specifying which site will be loaded
        :return: JSON response containing info about order.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.post(
            "/general/v3/order/",
            data=payload,
            headers={
                "token": site_token,
                "Content-Type": "application/json"
            }
        )

        return response
