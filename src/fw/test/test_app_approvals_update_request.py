# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fw.models.app_approvals_update_request import AppApprovalsUpdateRequest

class TestAppApprovalsUpdateRequest(unittest.TestCase):
    """AppApprovalsUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppApprovalsUpdateRequest:
        """Test AppApprovalsUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppApprovalsUpdateRequest`
        """
        model = AppApprovalsUpdateRequest()
        if include_optional:
            return AppApprovalsUpdateRequest(
                fields = fw.models.`field_mask`_represents_a_set_of_symbolic_field_paths,_for_example:.`FieldMask` represents a set of symbolic field paths, for example:(
                    paths = [
                        ''
                        ], ),
                inserted_approvals = [
                    fw.models.atcfw_app_approval.atcfwAppApproval(
                        app_name = '', 
                        status = '', )
                    ],
                removed_approvals = [
                    fw.models.atcfw_app_approval_removal_request.atcfwAppApprovalRemovalRequest(
                        app_name = '', )
                    ]
            )
        else:
            return AppApprovalsUpdateRequest(
        )
        """

    def testAppApprovalsUpdateRequest(self):
        """Test AppApprovalsUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()