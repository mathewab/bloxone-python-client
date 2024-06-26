# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dns_config.models.server_inheritance import ServerInheritance

class TestServerInheritance(unittest.TestCase):
    """ServerInheritance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerInheritance:
        """Test ServerInheritance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerInheritance`
        """
        model = ServerInheritance()
        if include_optional:
            return ServerInheritance(
                add_edns_option_in_outgoing_query = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                custom_root_ns_block = dns_config.models.inherited_custom_root_ns_block.InheritedCustomRootNSBlock(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = dns_config.models.custom_root_ns_block.CustomRootNSBlock(
                        custom_root_ns = [
                            dns_config.models.root_ns.RootNS(
                                address = '10.0.0.0', 
                                fqdn = 'example.com', 
                                protocol_fqdn = 'test.key.com.', )
                            ], 
                        custom_root_ns_enabled = True, ), ),
                dnssec_validation_block = dns_config.models.inherited_dnssec_validation_block.InheritedDNSSECValidationBlock(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = dns_config.models.dnssec_validation_block.DNSSECValidationBlock(
                        dnssec_enable_validation = True, 
                        dnssec_enabled = True, 
                        dnssec_trust_anchors = [
                            dns_config.models.trust_anchor.TrustAnchor(
                                algorithm = 56, 
                                protocol_zone = '', 
                                public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArGEl09qgDz+9YOH8Ff4Z', 
                                sep = True, 
                                zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4', )
                            ], 
                        dnssec_validate_expiry = True, ), ),
                ecs_block = dns_config.models.inherited_ecs_block.InheritedECSBlock(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = dns_config.models.ecs_block.ECSBlock(
                        ecs_enabled = True, 
                        ecs_forwarding = True, 
                        ecs_prefix_v4 = 56, 
                        ecs_prefix_v6 = 56, 
                        ecs_zones = [
                            dns_config.models.ecs_zone.ECSZone(
                                access = 'allow', 
                                fqdn = 'example.com', 
                                protocol_fqdn = '', )
                            ], ), ),
                filter_aaaa_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), )
                        ], ),
                filter_aaaa_on_v4 = dns_config.models.inherited_string.InheritedString(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = '', ),
                forwarders_block = dns_config.models.inherited_forwarders_block.InheritedForwardersBlock(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = dns_config.models.forwarders_block.ForwardersBlock(
                        forwarders = [
                            dns_config.models.forwarder.Forwarder(
                                address = '10.0.0.0', 
                                fqdn = 'ns1.example.com', 
                                protocol_fqdn = '', )
                            ], 
                        forwarders_only = True, 
                        use_root_forwarders_for_local_resolution_with_b1td = True, ), ),
                gss_tsig_enabled = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                kerberos_keys = dns_config.models.inherited_kerberos_keys.InheritedKerberosKeys(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.kerberos_key.KerberosKey(
                            algorithm = '', 
                            domain = '', 
                            key = 'keys/kerberos/23311109-fad4-448f-a7a7-55ad791ae7eb', 
                            principal = '', 
                            uploaded_at = '', 
                            version = 56, )
                        ], ),
                lame_ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                log_query_response = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                match_recursive_only = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                max_cache_ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                max_negative_ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                minimal_responses = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                notify = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                query_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), )
                        ], ),
                query_port = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                recursion_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), )
                        ], ),
                recursion_enabled = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                recursive_clients = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                resolver_query_timeout = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                secondary_axfr_query_limit = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                secondary_soa_query_limit = dns_config.models.inherited_u_int32.InheritedUInt32(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = 56, ),
                sort_list = dns_config.models.inherited_sort_list_items.InheritedSortListItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.sort_list_item.SortListItem(
                            acl = '', 
                            element = 'ip', 
                            prioritized_networks = [
                                ''
                                ], 
                            source = '', )
                        ], ),
                synthesize_address_records_from_https = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, ),
                transfer_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), )
                        ], ),
                update_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', 
                            tsig_key = dns_config.models.tsig_key.TSIGKey(
                                algorithm = '', 
                                comment = '', 
                                key = '', 
                                name = '', 
                                protocol_name = '', 
                                secret = '', ), )
                        ], ),
                use_forwarders_for_subzones = dns_config.models.inherited_bool.InheritedBool(
                    action = '', 
                    display_name = '', 
                    source = '', 
                    value = True, )
            )
        else:
            return ServerInheritance(
        )
        """

    def testServerInheritance(self):
        """Test ServerInheritance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
