# coding: utf-8

"""
    Infrastructure Management API

    The **Infrastructure Management API** provides a RESTful interface to manage Infrastructure Hosts and Services objects.  The following is a list of the different Services and their string types (the string types are to be used with the APIs for the `service_type` field):  | Service name | Service type |   | ------ | ------ |   | Access Authentication | authn |   | Anycast | anycast |   | Data Connector | cdc |   | DHCP | dhcp |   | DNS | dns |   | DNS Forwarding Proxy | dfp |   | NIOS Grid Connector | orpheus |   | MS AD Sync | msad |   | NTP | ntp |   | BGP | bgp |   | RIP | rip |   | OSPF | ospf |    ---   ### Hosts API  The Hosts API is used to manage the Infrastructure Host resources. These include various operations related to hosts such as viewing, creating, updating, replacing, disconnecting, and deleting Hosts. Management of Hosts is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Hosts tab.  ---   ### Services API  The Services API is used to manage the Infrastructure Service resources (a.k.a. BloxOne applications). These include various operations related to hosts such as viewing, creating, updating, starting/stopping, configuring, and deleting Services. Management of Services is done from the Cloud Services Portal (CSP) by navigating to the Manage -> Infrastructure -> Services tab.  ---   ### Detail APIs  The Detail APIs are read-only APIs used to list all the Infrastructure resources (Hosts and Services). Each resource record returned also contains information about its other associated resources and the status information for itself and the associated resource(s) (i.e., Host/Service status).  ---   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from infra_mgmt.api.services_api import ServicesApi


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServicesApi()

    def tearDown(self) -> None:
        pass

    def test_Applications(self) -> None:
        """Test case for Applications

        List applications (Service types) for a particular account.
        """
        pass

    def test_Create(self) -> None:
        """Test case for Create

        Create a Service resource.
        """
        pass

    def test_Delete(self) -> None:
        """Test case for Delete

        Delete a Service resource.
        """
        pass

    def test_List(self) -> None:
        """Test case for List

        List all the Service resources for an account.
        """
        pass

    def test_Read(self) -> None:
        """Test case for Read

        Read a Service resource.
        """
        pass

    def test_Update(self) -> None:
        """Test case for Update

        Update a Service resource.
        """
        pass


if __name__ == '__main__':
    unittest.main()