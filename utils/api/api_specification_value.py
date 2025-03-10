from playwright.sync_api import Playwright


def create_specification(playwright: Playwright, payload: dict, site_token: str, api_token: str):
    """
    Performs an API request to create a specification value.

    :param playwright: Playwright object used to create the API request context.
    :param payload: JSON data
    :param site_token: Identifier specifying which site will be loaded
    :param api_token: API authentication token
    :return: JSON response containing specification value.
    :raises AssertionError: If the API response is not successful. (response.ok == False).
    """
    api_request_context = playwright.request.new_context(
        base_url="https://stage.admin.ecom.md"
    )
    response = api_request_context.post(
        "/external/specification-value/bulk-create/",
        data=payload,
        headers={
            "token": site_token,
            "Content-Type": "application/json",
            "API-Token": api_token
        }
    )

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response_body = response.json()
    return response_body


def get_specifications_list(playwright: Playwright, site_token: str, api_token: str):
    """
    Performs an API request to retrieve a list of specification values.

    :param playwright: Playwright object used to create the API request context.
    :param site_token: Identifier specifying which site will be loaded
    :param api_token: API authentication token
    :return: A list of specification values in JSON format (key "results").
    :raises AssertionError: If the API response is not successful. (response.ok == False).
    """
    api_request_context = playwright.request.new_context(
        base_url="https://stage.admin.ecom.md"
    )
    response = api_request_context.get(
        "/external/specification-value/",
        headers={
            "token": site_token,
            "Content-Type": "application/json",
            "API-Token": api_token
        }
    )

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response_body = response.json()
    return response_body["results"]


def get_specification_details_by_id(playwright: Playwright, specification_value_id: str, site_token: str, api_token: str):
    """
    Performs an API request to retrieve the details of a specification value with specified ID.

    :param playwright: Playwright object used to create the API request context.
    :param specification_value_id: The ID of the specification value to retrieve.
    :param site_token: Identifier specifying which site will be loaded
    :param api_token: API authentication token
    :return: JSON response containing the specification value details.
    :raises AssertionError: If the API response is not successful. (response.ok == False).
    """
    api_request_context = playwright.request.new_context(
        base_url="https://stage.admin.ecom.md"
    )
    response = api_request_context.get(
        f"/external/specification-value/{specification_value_id}",
        headers={
            "token": site_token,
            "Content-Type": "application/json",
            "API-Token": api_token
        }
    )

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response_body = response.json()
    return response_body


def update_one_key_of_specification_with_id(playwright: Playwright, specification_value_id: str, payload: dict, site_token: str, api_token: str):
    """
    Performs an API request to update a single key of a specification value with selected ID.

    :param playwright: Playwright object used to create the API request context.
    :param specification_value_id: The ID of the specification value to update.
    :param payload: JSON data
    :param site_token: Identifier specifying which site will be loaded
    :param api_token: API authentication token
    :return: JSON response containing the updated specification value.
    :raises AssertionError: If the API response is not successful. (response.ok == False).
    """
    api_request_context = playwright.request.new_context(
        base_url="https://stage.admin.ecom.md"
    )
    response = api_request_context.put(
        f"/external/specification-value/{specification_value_id}/",
        data=payload,
        headers={
            "token": site_token,
            "Content-Type": "application/json",
            "API-Token": api_token
        }
    )

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"

    response_body = response.json()
    return response_body


def delete_specification_by_id(playwright: Playwright, specification_value_id: str, site_token: str, api_token: str):
    """
    Performs an API request to delete specification value with specified ID.

    :param playwright: Playwright object used to create the API request context.
    :param specification_value_id: The ID of the specification value to delete.
    :param site_token: Identifier specifying which site will be loaded
    :param api_token: API authentication token
    :raises AssertionError: If the API response is not successful. (response.ok == False).
    """
    api_request_context = playwright.request.new_context(
        base_url="https://stage.admin.ecom.md"
    )
    response = api_request_context.delete(
        f"/external/specification-value/{specification_value_id}/",
        headers={
            "token": site_token,
            "Content-Type": "application/json",
            "API-Token": api_token
        }
    )

    assert response.ok, f"API request failed with status {response.status}: {response.text()}"