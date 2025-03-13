import json
from playwright.sync_api import Playwright

from utilities.api.api_general_req import APIGeneral


class DataProcessing:

    def get_list_from_file(self, file_name, list_title):
        """
        Returns the list with data from the given file

        :param file_name: Give file name with its extension
        :param list_title: Give key name that has list value
        :return: List with data
        """
        with open("../data/" + file_name + "") as f:
            file_data = json.load(f)
            required_list = file_data[list_title]
        return required_list

    def get_site_params_from_list(self, site_data, site_name):
        """
        Form a JSON with site settings in special order from which it can be acquired what
        to do, run or skip the test

        :param site_data: JSON response from global site settings request
        :param site_name: Name of the site that will be added to indicate which site params it is
        :return: JSON with site settings
        """
        main_ui_interface = site_data["mainUiInterface"]
        additional_settings = site_data["additional_settings"]

        return {
            "name": site_name,
            "main_navigation_type": main_ui_interface["mainNavigationType"],
            "top_navigation_type": main_ui_interface["topNavigationType"],
            "is_user_cabinet": additional_settings["is_user_cabinet"],
        }

    def save_site_params_to_file(self, playwright: Playwright, site_list):
        """
        Saves each site settings in the file in JSON format

        :param playwright: Global fixture
        :param site_list: Dictionary with site's name and token
        :return:
        """
        api_general = APIGeneral()
        site_params_list = []
        # Get the setting of all the sites in the list
        for site in site_list:
            site_data = api_general.get_global_site_settings(playwright, site["token"])
            site_params = self.get_site_params_from_list(site_data, site["project"])
            # Save the data ib the list
            site_params_list.append(site_params)
        # After the loop write the given data from the list in to the file
        result = {"site_params": site_params_list}
        with open("../data/site_params.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    def get_selected_site_param_from_file(self, name):
        """
        Get selected site settings from the file

        :param name: Site name that is listed in the file "site_params.json"
        :return: Dictionary with site settings of selected site
        """
        with open("../data/site_params.json", 'r') as file:
            data = json.load(file)
            site_params = data["site_params"]

        for param in site_params:
            if param["name"] == name:
                site_param = param
                return site_param

    def get_payload_from_file(self, file_name, list_title):
        with open("../data/" + file_name + "") as f:
            file_data = json.load(f)
            required_list = file_data[list_title]
        return required_list
