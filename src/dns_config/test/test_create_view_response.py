# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dns_config.models.create_view_response import CreateViewResponse

class TestCreateViewResponse(unittest.TestCase):
    """CreateViewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateViewResponse:
        """Test CreateViewResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateViewResponse`
        """
        model = CreateViewResponse()
        if include_optional:
            return CreateViewResponse(
                result = dns_config.models.view.View(
                    add_edns_option_in_outgoing_query = True, 
                    comment = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    custom_root_ns = [
                        dns_config.models.root_ns.RootNS(
                            address = '10.0.0.0', 
                            fqdn = 'example.com', 
                            protocol_fqdn = 'test.key.com.', )
                        ], 
                    custom_root_ns_enabled = True, 
                    disabled = True, 
                    dnssec_enable_validation = True, 
                    dnssec_enabled = True, 
                    dnssec_root_keys = [
                        dns_config.models.trust_anchor.TrustAnchor(
                            algorithm = 56, 
                            protocol_zone = '', 
                            public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArGEl09qgDz+9YOH8Ff4Z', 
                            sep = True, 
                            zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4', )
                        ], 
                    dnssec_trust_anchors = [
                        dns_config.models.trust_anchor.TrustAnchor(
                            algorithm = 56, 
                            protocol_zone = '', 
                            public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArGEl09qgDz+9YOH8Ff4Z', 
                            sep = True, 
                            zone = 'dns/auth_zone/16d9158d-d0d7-48e1-9a55-087e7aa419d4', )
                        ], 
                    dnssec_validate_expiry = True, 
                    dtc_config = dns_config.models.dtc_config.DTCConfig(
                        default_ttl = 56, ), 
                    ecs_enabled = True, 
                    ecs_forwarding = True, 
                    ecs_prefix_v4 = 56, 
                    ecs_prefix_v6 = 56, 
                    ecs_zones = [
                        dns_config.models.ecs_zone.ECSZone(
                            access = 'allow', 
                            fqdn = 'example.com', 
                            protocol_fqdn = '', )
                        ], 
                    edns_udp_size = 56, 
                    filter_aaaa_acl = [
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
                        ], 
                    filter_aaaa_on_v4 = '', 
                    forwarders = [
                        dns_config.models.forwarder.Forwarder(
                            address = '10.0.0.0', 
                            fqdn = 'ns1.example.com', 
                            protocol_fqdn = '', )
                        ], 
                    forwarders_only = True, 
                    gss_tsig_enabled = True, 
                    id = '', 
                    inheritance_sources = dns_config.models.view_inheritance.ViewInheritance(
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
                                custom_root_ns_enabled = True, ), ), 
                        dnssec_validation_block = dns_config.models.inherited_dnssec_validation_block.InheritedDNSSECValidationBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        ecs_block = dns_config.models.inherited_ecs_block.InheritedECSBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        edns_udp_size = dns_config.models.inherited_u_int32.InheritedUInt32(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        filter_aaaa_on_v4 = dns_config.models.inherited_string.InheritedString(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        forwarders_block = dns_config.models.inherited_forwarders_block.InheritedForwardersBlock(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        gss_tsig_enabled = dns_config.models.inherited_bool.InheritedBool(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        lame_ttl = dns_config.models.inherited_u_int32.InheritedUInt32(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        match_recursive_only = , 
                        max_cache_ttl = , 
                        max_negative_ttl = , 
                        max_udp_size = , 
                        minimal_responses = , 
                        notify = , 
                        query_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        recursion_acl = dns_config.models.inherited_acl_items.InheritedACLItems(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        recursion_enabled = , 
                        sort_list = dns_config.models.inherited_sort_list_items.InheritedSortListItems(
                            action = '', 
                            display_name = '', 
                            source = '', ), 
                        synthesize_address_records_from_https = , 
                        transfer_acl = , 
                        update_acl = , 
                        use_forwarders_for_subzones = , 
                        zone_authority = dns_config.models.inherited_zone_authority.InheritedZoneAuthority(
                            default_ttl = , 
                            expire = , 
                            mname_block = dns_config.models.inherited_authority_m_name_block.InheritedAuthorityMNameBlock(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            negative_ttl = , 
                            protocol_rname = dns_config.models.inherited_string.InheritedString(
                                action = '', 
                                display_name = '', 
                                source = '', ), 
                            refresh = , 
                            retry = , 
                            rname = , ), ), 
                    ip_spaces = [
                        ''
                        ], 
                    lame_ttl = 56, 
                    match_clients_acl = [
                        dns_config.models.acl_item.ACLItem(
                            access = 'allow', 
                            acl = '', 
                            address = '', 
                            element = 'ip', )
                        ], 
                    match_destinations_acl = [
                        
                        ], 
                    match_recursive_only = True, 
                    max_cache_ttl = 56, 
                    max_negative_ttl = 56, 
                    max_udp_size = 56, 
                    minimal_responses = True, 
                    name = 'Example Config View', 
                    notify = True, 
                    query_acl = [
                        
                        ], 
                    recursion_acl = [
                        
                        ], 
                    recursion_enabled = True, 
                    sort_list = [
                        dns_config.models.sort_list_item.SortListItem(
                            acl = '', 
                            element = 'ip', 
                            prioritized_networks = [
                                ''
                                ], 
                            source = '', )
                        ], 
                    synthesize_address_records_from_https = True, 
                    tags = dns_config.models.tags.tags(), 
                    transfer_acl = [
                        
                        ], 
                    update_acl = [
                        
                        ], 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    use_forwarders_for_subzones = True, 
                    use_root_forwarders_for_local_resolution_with_b1td = True, 
                    zone_authority = dns_config.models.zone_authority.ZoneAuthority(
                        mname = '', 
                        protocol_mname = '', 
                        use_default_mname = True, ), )
            )
        else:
            return CreateViewResponse(
        )
        """

    def testCreateViewResponse(self):
        """Test CreateViewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()