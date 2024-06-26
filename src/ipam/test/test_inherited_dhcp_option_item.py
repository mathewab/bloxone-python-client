# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipam.models.inherited_dhcp_option_item import InheritedDHCPOptionItem

class TestInheritedDHCPOptionItem(unittest.TestCase):
    """InheritedDHCPOptionItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InheritedDHCPOptionItem:
        """Test InheritedDHCPOptionItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InheritedDHCPOptionItem`
        """
        model = InheritedDHCPOptionItem()
        if include_optional:
            return InheritedDHCPOptionItem(
                option = ipam.models.option_item.OptionItem(
                    group = '', 
                    option_code = '', 
                    option_value = '', 
                    type = '', ),
                overriding_group = ''
            )
        else:
            return InheritedDHCPOptionItem(
        )
        """

    def testInheritedDHCPOptionItem(self):
        """Test InheritedDHCPOptionItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
