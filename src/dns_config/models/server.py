# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a Universal DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured Universal DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dns_config.models.acl_item import ACLItem
from dns_config.models.display_view import DisplayView
from dns_config.models.ecs_zone import ECSZone
from dns_config.models.forwarder import Forwarder
from dns_config.models.kerberos_key import KerberosKey
from dns_config.models.root_ns import RootNS
from dns_config.models.server_inheritance import ServerInheritance
from dns_config.models.sort_list_item import SortListItem
from dns_config.models.trust_anchor import TrustAnchor
from typing import Optional, Set
from typing_extensions import Self


class Server(BaseModel):
    """
    A DNS Config Profile (_dns/server_) is a named configuration for specified list of hosts.
    """ # noqa: E501
    add_edns_option_in_outgoing_query: Optional[StrictBool] = Field(
        default=None,
        description=
        "_add_edns_option_in_outgoing_query_ adds client IP, MAC address and view name into outgoing recursive query. Defaults to _false_."
    )
    auto_sort_views: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. Controls manual/automatic views ordering.  Defaults to _true_."
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Optional. Comment for configuration.")
    created_at: Optional[datetime] = Field(
        default=None, description="Time when the object has been created.")
    custom_root_ns: Optional[List[RootNS]] = Field(
        default=None,
        description=
        "Optional. List of custom root nameservers. The order does not matter.  Error if empty while _custom_root_ns_enabled_ is _true_. Error if there are duplicate items in the list.  Defaults to empty."
    )
    custom_root_ns_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to use custom root nameservers instead of the default ones.  The _custom_root_ns_ is validated when enabled.  Defaults to _false_."
    )
    dnssec_enable_validation: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to perform DNSSEC validation. Ignored if _dnssec_enabled_ is _false_.  Defaults to _true_."
    )
    dnssec_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. Master toggle for all DNSSEC processing. Other _dnssec_*_ configuration is unused if this is disabled.  Defaults to _true_."
    )
    dnssec_root_keys: Optional[List[TrustAnchor]] = Field(
        default=None,
        description=
        "DNSSEC root keys. The root keys are not configurable.  A default list is provided by cloud management and included here for config generation."
    )
    dnssec_trust_anchors: Optional[List[TrustAnchor]] = Field(
        default=None,
        description=
        "Optional. DNSSEC trust anchors.  Error if there are list items with duplicate (_zone_, _sep_, _algorithm_) combinations.  Defaults to empty."
    )
    dnssec_validate_expiry: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to reject expired DNSSEC keys. Ignored if either _dnssec_enabled_ or _dnssec_enable_validation_ is _false_.  Defaults to _true_."
    )
    ecs_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to enable EDNS client subnet for recursive queries. Other _ecs_*_ fields are ignored if this field is not enabled.  Defaults to _false_."
    )
    ecs_forwarding: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to enable ECS options in outbound queries. This functionality has additional overhead so it is disabled by default.  Defaults to _false_."
    )
    ecs_prefix_v4: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Maximum scope length for v4 ECS.  Unsigned integer, min 1 max 24  Defaults to 24."
    )
    ecs_prefix_v6: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Maximum scope length for v6 ECS.  Unsigned integer, min 1 max 56  Defaults to 56."
    )
    ecs_zones: Optional[List[ECSZone]] = Field(
        default=None,
        description=
        "Optional. List of zones where ECS queries may be sent.  Error if empty while _ecs_enabled_ is _true_. Error if there are duplicate FQDNs in the list.  Defaults to empty."
    )
    filter_aaaa_acl: Optional[List[ACLItem]] = Field(
        default=None,
        description=
        "Optional. Specifies a list of client addresses for which AAAA filtering is to be applied.  Defaults to _empty_."
    )
    filter_aaaa_on_v4: Optional[StrictStr] = Field(
        default=None,
        description=
        "_filter_aaaa_on_v4_ allows named to omit some IPv6 addresses when responding to IPv4 clients.  Allowed values: * _yes_, * _no_, * _break_dnssec_.  Defaults to _no_"
    )
    forwarders: Optional[List[Forwarder]] = Field(
        default=None,
        description=
        "Optional. List of forwarders.  Error if empty while _forwarders_only_ or _use_root_forwarders_for_local_resolution_with_b1td_ is _true_. Error if there are items in the list with duplicate addresses.  Defaults to empty."
    )
    forwarders_only: Optional[StrictBool] = Field(
        default=None,
        description="Optional. _true_ to only forward.  Defaults to _false_.")
    gss_tsig_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "_gss_tsig_enabled_ enables/disables GSS-TSIG signed dynamic updates.  Defaults to _false_."
    )
    id: Optional[StrictStr] = Field(default=None,
                                    description="The resource identifier.")
    inheritance_sources: Optional[ServerInheritance] = Field(
        default=None, description="Optional. Inheritance configuration.")
    kerberos_keys: Optional[List[KerberosKey]] = Field(
        default=None,
        description=
        "_kerberos_keys_ contains a list of keys for GSS-TSIG signed dynamic updates.  Defaults to empty."
    )
    lame_ttl: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Unused in the current on-prem DNS server implementation.  Unsigned integer, min 0 max 3600 (1h).  Defaults to 600."
    )
    log_query_response: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. Control DNS query/response logging functionality.  Defaults to _true_."
    )
    match_recursive_only: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. If _true_ only recursive queries from matching clients access the view.  Defaults to _false_."
    )
    max_cache_ttl: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Seconds to cache positive responses.  Unsigned integer, min 1 max 604800 (7d).  Defaults to 604800 (7d)."
    )
    max_negative_ttl: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Seconds to cache negative responses.  Unsigned integer, min 1 max 604800 (7d).  Defaults to 10800 (3h)."
    )
    minimal_responses: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. When enabled, the DNS server will only add records to the authority and additional data sections when they are required.  Defaults to _false_."
    )
    name: StrictStr = Field(description="Name of configuration.")
    notify: Optional[StrictBool] = Field(
        default=None,
        description=
        "_notify_ all external secondary DNS servers.  Defaults to _false_.")
    query_acl: Optional[List[ACLItem]] = Field(
        default=None,
        description=
        "Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset.  Defaults to empty."
    )
    query_port: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Source port for outbound DNS queries. When set to 0 the port is unspecified and the implementation may randomize it using any available ports.  Defaults to 0."
    )
    recursion_acl: Optional[List[ACLItem]] = Field(
        default=None,
        description=
        "Optional. Clients must match this ACL to make recursive queries. If this ACL is empty, then the _query_acl_ field will be used instead.  Defaults to empty."
    )
    recursion_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. _true_ to allow recursive DNS queries.  Defaults to _true_."
    )
    recursive_clients: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Defines the number of simultaneous recursive lookups the server will perform on behalf of its clients.  Defaults to 1000."
    )
    resolver_query_timeout: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Seconds before a recursive query times out.  Unsigned integer, min 10 max 30.  Defaults to 10."
    )
    secondary_axfr_query_limit: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Maximum concurrent inbound AXFRs. When set to 0 a host-dependent default will be used.  Defaults to 0."
    )
    secondary_soa_query_limit: Optional[StrictInt] = Field(
        default=None,
        description=
        "Optional. Maximum concurrent outbound SOA queries. When set to 0 a host-dependent default will be used.  Defaults to 0."
    )
    sort_list: Optional[List[SortListItem]] = Field(
        default=None,
        description=
        "Optional. Specifies a sorted network list for A/AAAA records in DNS query response.  Defaults to _empty_."
    )
    synthesize_address_records_from_https: Optional[StrictBool] = Field(
        default=None,
        description=
        "_synthesize_address_records_from_https_ enables/disables creation of A/AAAA records from HTTPS RR Defaults to _false_."
    )
    tags: Optional[Dict[str, Any]] = Field(default=None,
                                           description="Tagging specifics.")
    transfer_acl: Optional[List[ACLItem]] = Field(
        default=None,
        description=
        "Optional. Clients must match this ACL to receive zone transfers.  Defaults to empty."
    )
    update_acl: Optional[List[ACLItem]] = Field(
        default=None,
        description=
        "Optional. Specifies which hosts are allowed to issue Dynamic DNS updates for authoritative zones of _primary_type_ _cloud_.  Defaults to empty."
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        description=
        "Time when the object has been updated. Equals to _created_at_ if not updated after creation."
    )
    use_forwarders_for_subzones: Optional[StrictBool] = Field(
        default=None,
        description=
        "Optional. Use default forwarders to resolve queries for subzones.  Defaults to _true_."
    )
    use_root_forwarders_for_local_resolution_with_b1td: Optional[
        StrictBool] = Field(
            default=None,
            description=
            "_use_root_forwarders_for_local_resolution_with_b1td_ allows DNS recursive queries sent to root forwarders for local resolution when deployed alongside BloxOne Thread Defense. Defaults to _false_."
        )
    views: Optional[List[DisplayView]] = Field(
        default=None,
        description=
        "Optional. Ordered list of _dns/display_view_ objects served by any of _dns/host_ assigned to a particular DNS Config Profile. Automatically determined. Allows re-ordering only."
    )
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "add_edns_option_in_outgoing_query", "auto_sort_views", "comment",
        "created_at", "custom_root_ns", "custom_root_ns_enabled",
        "dnssec_enable_validation", "dnssec_enabled", "dnssec_root_keys",
        "dnssec_trust_anchors", "dnssec_validate_expiry", "ecs_enabled",
        "ecs_forwarding", "ecs_prefix_v4", "ecs_prefix_v6", "ecs_zones",
        "filter_aaaa_acl", "filter_aaaa_on_v4", "forwarders",
        "forwarders_only", "gss_tsig_enabled", "id", "inheritance_sources",
        "kerberos_keys", "lame_ttl", "log_query_response",
        "match_recursive_only", "max_cache_ttl", "max_negative_ttl",
        "minimal_responses", "name", "notify", "query_acl", "query_port",
        "recursion_acl", "recursion_enabled", "recursive_clients",
        "resolver_query_timeout", "secondary_axfr_query_limit",
        "secondary_soa_query_limit", "sort_list",
        "synthesize_address_records_from_https", "tags", "transfer_acl",
        "update_acl", "updated_at", "use_forwarders_for_subzones",
        "use_root_forwarders_for_local_resolution_with_b1td", "views"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Server from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "dnssec_root_keys",
            "id",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in custom_root_ns (list)
        _items = []
        if self.custom_root_ns:
            for _item in self.custom_root_ns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_root_ns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dnssec_root_keys (list)
        _items = []
        if self.dnssec_root_keys:
            for _item in self.dnssec_root_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dnssec_root_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dnssec_trust_anchors (list)
        _items = []
        if self.dnssec_trust_anchors:
            for _item in self.dnssec_trust_anchors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dnssec_trust_anchors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ecs_zones (list)
        _items = []
        if self.ecs_zones:
            for _item in self.ecs_zones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ecs_zones'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filter_aaaa_acl (list)
        _items = []
        if self.filter_aaaa_acl:
            for _item in self.filter_aaaa_acl:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filter_aaaa_acl'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in forwarders (list)
        _items = []
        if self.forwarders:
            for _item in self.forwarders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['forwarders'] = _items
        # override the default output from pydantic by calling `to_dict()` of inheritance_sources
        if self.inheritance_sources:
            _dict['inheritance_sources'] = self.inheritance_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in kerberos_keys (list)
        _items = []
        if self.kerberos_keys:
            for _item in self.kerberos_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['kerberos_keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in query_acl (list)
        _items = []
        if self.query_acl:
            for _item in self.query_acl:
                if _item:
                    _items.append(_item.to_dict())
            _dict['query_acl'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recursion_acl (list)
        _items = []
        if self.recursion_acl:
            for _item in self.recursion_acl:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recursion_acl'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sort_list (list)
        _items = []
        if self.sort_list:
            for _item in self.sort_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sort_list'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transfer_acl (list)
        _items = []
        if self.transfer_acl:
            for _item in self.transfer_acl:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transfer_acl'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in update_acl (list)
        _items = []
        if self.update_acl:
            for _item in self.update_acl:
                if _item:
                    _items.append(_item.to_dict())
            _dict['update_acl'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Server from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "add_edns_option_in_outgoing_query":
            obj.get("add_edns_option_in_outgoing_query"),
            "auto_sort_views":
            obj.get("auto_sort_views"),
            "comment":
            obj.get("comment"),
            "created_at":
            obj.get("created_at"),
            "custom_root_ns":
            [RootNS.from_dict(_item) for _item in obj["custom_root_ns"]]
            if obj.get("custom_root_ns") is not None else None,
            "custom_root_ns_enabled":
            obj.get("custom_root_ns_enabled"),
            "dnssec_enable_validation":
            obj.get("dnssec_enable_validation"),
            "dnssec_enabled":
            obj.get("dnssec_enabled"),
            "dnssec_root_keys": [
                TrustAnchor.from_dict(_item)
                for _item in obj["dnssec_root_keys"]
            ] if obj.get("dnssec_root_keys") is not None else None,
            "dnssec_trust_anchors": [
                TrustAnchor.from_dict(_item)
                for _item in obj["dnssec_trust_anchors"]
            ] if obj.get("dnssec_trust_anchors") is not None else None,
            "dnssec_validate_expiry":
            obj.get("dnssec_validate_expiry"),
            "ecs_enabled":
            obj.get("ecs_enabled"),
            "ecs_forwarding":
            obj.get("ecs_forwarding"),
            "ecs_prefix_v4":
            obj.get("ecs_prefix_v4"),
            "ecs_prefix_v6":
            obj.get("ecs_prefix_v6"),
            "ecs_zones":
            [ECSZone.from_dict(_item) for _item in obj["ecs_zones"]]
            if obj.get("ecs_zones") is not None else None,
            "filter_aaaa_acl":
            [ACLItem.from_dict(_item) for _item in obj["filter_aaaa_acl"]]
            if obj.get("filter_aaaa_acl") is not None else None,
            "filter_aaaa_on_v4":
            obj.get("filter_aaaa_on_v4"),
            "forwarders":
            [Forwarder.from_dict(_item) for _item in obj["forwarders"]]
            if obj.get("forwarders") is not None else None,
            "forwarders_only":
            obj.get("forwarders_only"),
            "gss_tsig_enabled":
            obj.get("gss_tsig_enabled"),
            "id":
            obj.get("id"),
            "inheritance_sources":
            ServerInheritance.from_dict(obj["inheritance_sources"])
            if obj.get("inheritance_sources") is not None else None,
            "kerberos_keys":
            [KerberosKey.from_dict(_item) for _item in obj["kerberos_keys"]]
            if obj.get("kerberos_keys") is not None else None,
            "lame_ttl":
            obj.get("lame_ttl"),
            "log_query_response":
            obj.get("log_query_response"),
            "match_recursive_only":
            obj.get("match_recursive_only"),
            "max_cache_ttl":
            obj.get("max_cache_ttl"),
            "max_negative_ttl":
            obj.get("max_negative_ttl"),
            "minimal_responses":
            obj.get("minimal_responses"),
            "name":
            obj.get("name"),
            "notify":
            obj.get("notify"),
            "query_acl":
            [ACLItem.from_dict(_item) for _item in obj["query_acl"]]
            if obj.get("query_acl") is not None else None,
            "query_port":
            obj.get("query_port"),
            "recursion_acl":
            [ACLItem.from_dict(_item) for _item in obj["recursion_acl"]]
            if obj.get("recursion_acl") is not None else None,
            "recursion_enabled":
            obj.get("recursion_enabled"),
            "recursive_clients":
            obj.get("recursive_clients"),
            "resolver_query_timeout":
            obj.get("resolver_query_timeout"),
            "secondary_axfr_query_limit":
            obj.get("secondary_axfr_query_limit"),
            "secondary_soa_query_limit":
            obj.get("secondary_soa_query_limit"),
            "sort_list":
            [SortListItem.from_dict(_item) for _item in obj["sort_list"]]
            if obj.get("sort_list") is not None else None,
            "synthesize_address_records_from_https":
            obj.get("synthesize_address_records_from_https"),
            "tags":
            obj.get("tags"),
            "transfer_acl":
            [ACLItem.from_dict(_item) for _item in obj["transfer_acl"]]
            if obj.get("transfer_acl") is not None else None,
            "update_acl":
            [ACLItem.from_dict(_item) for _item in obj["update_acl"]]
            if obj.get("update_acl") is not None else None,
            "updated_at":
            obj.get("updated_at"),
            "use_forwarders_for_subzones":
            obj.get("use_forwarders_for_subzones"),
            "use_root_forwarders_for_local_resolution_with_b1td":
            obj.get("use_root_forwarders_for_local_resolution_with_b1td"),
            "views": [DisplayView.from_dict(_item) for _item in obj["views"]]
            if obj.get("views") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
