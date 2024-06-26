# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipam.models.dhcp_info import DHCPInfo

class TestDHCPInfo(unittest.TestCase):
    """DHCPInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DHCPInfo:
        """Test DHCPInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DHCPInfo`
        """
        model = DHCPInfo()
        if include_optional:
            return DHCPInfo(
                client_hostname = '',
                client_hwaddr = '',
                client_id = '',
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fingerprint = '',
                iaid = 56,
                lease_type = '',
                preferred_lifetime = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                remain = 56,
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = '',
                state_ts = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DHCPInfo(
        )
        """

    def testDHCPInfo(self):
        """Test DHCPInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
