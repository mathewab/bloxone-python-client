# coding: utf-8

"""
    Discovery Configuration API V2

    The Discovery configuration service is a Universal DDI Service that provides configuration for accessing and syncing the Cloud assets   Base Paths:  1. provider: **/api/cloud_discovery/v2/**  

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from cloud_discovery.api.sub_accounts_api import SubAccountsApi

from universal_ddi_client.api_client import ApiClient


class TestSubAccountsApi(unittest.TestCase):
    """SubAccountsApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = SubAccountsApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_list(self) -> None:
        """Test case for list

        List Sub-accounts
        """
        pass


if __name__ == '__main__':
    unittest.main()
