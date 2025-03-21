from playwright.sync_api import Playwright


class APIGeneral:

    def get_global_site_settings(self, playwright: Playwright, site_token: str):
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md/"
        )
        response = api_request_context.get(
            "settings/global_site_settings",
            headers={
                "token": site_token,
                "Content-Type": "application/json"
            }
        )

        return response

    def clear_site_cache(self, playwright: Playwright, site_id: str):
        """
        Performs an API request to clear the site cache.

        :param site_id:
        :param playwright: Playwright object used to create the API request context.
        :return: JSON response containing the result of the cache clearing.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.post(
            "/ver4/clear_site_cache",
            form={
                "group_id": site_id
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )

        return response


    def get_order_data(self, playwright: Playwright, order_id: str, api_token: str):
        """
        Performs an API request to clear the site cache.

        :param order_id: ID ot the order
        :param playwright: Playwright object used to create the API request context.
        :return: JSON response containing the result of the cache clearing.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.get(
            f"/external/external-order/{order_id}",
            headers={
                "Content-Type": "application/json",
                "API-Token": api_token
            }
        )

        return response
