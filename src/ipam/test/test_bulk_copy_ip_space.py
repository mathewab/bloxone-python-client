# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipam.models.bulk_copy_ip_space import BulkCopyIPSpace

class TestBulkCopyIPSpace(unittest.TestCase):
    """BulkCopyIPSpace unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BulkCopyIPSpace:
        """Test BulkCopyIPSpace
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkCopyIPSpace`
        """
        model = BulkCopyIPSpace()
        if include_optional:
            return BulkCopyIPSpace(
                copy_dhcp_options = True,
                copy_objects = [ipam/subnet/d1606f5a-b6f5-4bcb-9585-641b5c063995, ipam/subnet/c8566b79-e312-4fcd-a766-81bdd1f70b35],
                recursive = True,
                skip_on_error = True,
                target = 'ipam/ip_space/6ef9db92-99fa-4ca0-a36e-749760a38d29'
            )
        else:
            return BulkCopyIPSpace(
                copy_objects = [ipam/subnet/d1606f5a-b6f5-4bcb-9585-641b5c063995, ipam/subnet/c8566b79-e312-4fcd-a766-81bdd1f70b35],
                target = 'ipam/ip_space/6ef9db92-99fa-4ca0-a36e-749760a38d29',
        )
        """

    def testBulkCopyIPSpace(self):
        """Test BulkCopyIPSpace"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
