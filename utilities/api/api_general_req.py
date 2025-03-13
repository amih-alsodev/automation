from playwright.sync_api import Playwright

class APIGeneral:

    def get_global_site_settings(self, playwright: Playwright, token):
        api_request_context = playwright.request.new_context(
            base_url="https://stage.admin.ecom.md/"
        )
        response = api_request_context.get(
            "settings/global_site_settings",
            headers={
                "token": token,
                "Content-Type": "application/json"
            }
        )

        assert response.ok

        response_body = response.json()
        return response_body
