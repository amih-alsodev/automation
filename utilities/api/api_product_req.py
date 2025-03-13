from playwright.sync_api import Playwright


class APIProduct:

    def create_product(self, playwright: Playwright, payload: dict, site_token: str, api_token: str):
        """
        Performs an API request to create a product.

        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :param site_token: Identifier specifying which site will be loaded
        :param api_token: API authentication token
        :return: JSON response containing category.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.post(
            "/external/product/bulk-create/",
            data=payload,
            headers={
                "token": site_token,
                "Content-Type": "application/json",
                "API-Token": api_token
            }
        )

        return response

    def get_product_list(self, playwright: Playwright, site_token: str, api_token: str, page: int = None):
        """
        Performs an API request to retrieve a list of products.

        :param playwright: Playwright object used to create the API request context.
        :param site_token: Identifier specifying which site will be loaded
        :param api_token: API authentication token
        :param page: Not required query param for list page number
        :return: A list of products in JSON format (key "results").
        :raises AssertionError: If the API response is not successful (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )

        # Подготовка параметров запроса, если page передан
        params = {}
        if page is not None:
            params["page"] = page

        response = api_request_context.get(
            "/external/product/",
            headers={
                "token": site_token,
                "Content-Type": "application/json",
                "API-Token": api_token
            },
            params=params
        )

        return response

    def get_product_by_id(self, playwright: Playwright, product_id: str, site_token: str, api_token: str):
        """
        Performs an API request to retrieve product details by its ID.

        :param playwright: Playwright object used to create the API request context.
        :param product_id: The ID of the product to retrieve.
        :param site_token: Identifier specifying which site will be loaded
        :param api_token: API authentication token
        :return: JSON response containing the product details.
        :raises AssertionError: If the API response is not successful (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.get(
            f"/external/product/{product_id}",
            headers={
                "token": site_token,
                "Content-Type": "application/json",
                "API-Token": api_token
            }
        )

        return response

    def update_one_key_of_product_with_id(self, playwright: Playwright, payload, site_token: str, api_token: str):
        """
        Performs an API request to update a single key of a product with selected ID.

        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :param site_token: Identifier specifying which site will be loaded
        :param api_token: API authentication token
        :return: JSON response containing the updated product details.
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.post(
            "/external/product/bulk-create/",
            data=payload,
            headers={
                "token": site_token,
                "Content-Type": "application/json",
                "API-Token": api_token
            }
        )

        return response

    def delete_product_by_id(self, playwright: Playwright, product_id: str, site_token: str, api_token: str):
        """
        Performs an API request to delete category with specified ID.

        :param playwright: Playwright object used to create the API request context.
        :param product_id: The ID of the product to delete.
        :param site_token: Identifier specifying which site will be loaded
        :param api_token: API authentication token
        :raises AssertionError: If the API response is not successful. (response.ok == False).
        """
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md"
        )
        response = api_request_context.delete(
            f"/external/product/{product_id}/",
            headers={
                "token": site_token,
                "Content-Type": "application/json",
                "API-Token": api_token
            }
        )

        return response
