# coding: utf-8

"""
    Infoblox FW API

    Infoblox Threat Defense Cloud is an extension of the Infoblox Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to Infoblox Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. Infoblox Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

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
from fw.models.net_addr_dfp_assignment import NetAddrDfpAssignment
from fw.models.security_policy_rule import SecurityPolicyRule
from typing import Optional, Set
from typing_extensions import Self


class SecurityPolicy(BaseModel):
    """
    The Security Policy object.  A security policy defines a set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks. When you create a new security policy, you first define a network scope to which you add networks, DNS forwarding proxies, and Infoblox Endpoint groups. Infoblox Cloud applies the security policy to all the entities that you include in the network scope. You can also include DNS forwarding proxies to which you want to apply the security policy.  After you define the network scope, you can add custom lists and category filters to the security policy. You can also specify actions for the added lists and filters, and to determine the precedence order for the entities. Depending on your subscription level, each security policy also comes with a set of predefined threat intelligence feeds and Threat Insight rules that are inherited from the default global policy. You cannot delete the inherited feeds and rules, but you can change their precedence order. For each policy you can define policy-level action (Default Action) gets applied when none of the policy rules apply/match. If an user really needs access to some blocked domain (web page) via a browser - there is a possibility to assign special bypass code(s) (Bypass Code) to any policy.
    """ # noqa: E501
    access_codes: Optional[List[StrictStr]] = Field(
        default=None, description="Access codes assigned to Security Policy")
    created_time: Optional[datetime] = Field(
        default=None,
        description="The time when this Security Policy object was created.")
    default_action: Optional[StrictStr] = Field(
        default=None,
        description=
        "The policy-level action gets applied when none of the policy rules apply/match. The default value for default_action is \"action_allow\"."
    )
    default_redirect_name: Optional[StrictStr] = Field(
        default=None,
        description=
        "Name of the custom redirect, if the default_action is \"action_redirect\"."
    )
    description: Optional[StrictStr] = Field(
        default=None,
        description="The brief description for the security policy.")
    dfp_services: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "The list of DNS Forwarding Proxy Services object identifiers. For Internal Use only."
    )
    dfps: Optional[List[StrictInt]] = Field(
        default=None,
        description="The list of DNS Forwarding Proxy object identifiers.")
    ecs: Optional[StrictBool] = Field(
        default=None, description="Use ECS for handling policy")
    id: Optional[StrictInt] = Field(
        default=None, description="The Security Policy object identifier.")
    is_default: Optional[StrictBool] = Field(
        default=None,
        description=
        "Flag that indicates whether this is a default security policy.")
    name: Optional[StrictStr] = Field(
        default=None, description="The name of the security policy.")
    net_address_dfps: Optional[List[NetAddrDfpAssignment]] = Field(
        default=None,
        description=
        "List of DFPs associated with this policy via network address (with corresponding network address)"
    )
    network_lists: Optional[List[StrictInt]] = Field(
        default=None,
        description=
        "The list of Network Lists identifiers that represents networks that you want to protect from malicious attacks."
    )
    onprem_resolve: Optional[StrictBool] = Field(
        default=None, description="Use DNS resolve on onprem side")
    precedence: Optional[StrictInt] = Field(
        default=None,
        description=
        "Security precedence enable selection of the highest priority policy, in cases where a query matches multiple policies."
    )
    roaming_device_groups: Optional[List[StrictInt]] = Field(
        default=None,
        description="The list of Infoblox Endpoint groups identifiers.")
    rules: Optional[List[SecurityPolicyRule]] = Field(
        default=None,
        description=
        "The list of Security Policy Rules objects that represent the set of rules and actions that you define to balance access and constraints so you can mitigate malicious attacks and provide security for your networks."
    )
    safe_search: Optional[StrictBool] = Field(
        default=None,
        description="Apply automated rules to enforce safe search")
    tags: Optional[Dict[str, Any]] = Field(
        default=None,
        description=
        "Enables tag support for resource where tags attribute contains user-defined key value pairs"
    )
    updated_time: Optional[datetime] = Field(
        default=None,
        description=
        "The time when this Security Policy object was last updated.")
    user_groups: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of user groups associated with this policy")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "access_codes", "created_time", "default_action",
        "default_redirect_name", "description", "dfp_services", "dfps", "ecs",
        "id", "is_default", "name", "net_address_dfps", "network_lists",
        "onprem_resolve", "precedence", "roaming_device_groups", "rules",
        "safe_search", "tags", "updated_time", "user_groups"
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
        """Create an instance of SecurityPolicy from a JSON string"""
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
            "created_time",
            "id",
            "is_default",
            "updated_time",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in net_address_dfps (list)
        _items = []
        if self.net_address_dfps:
            for _item in self.net_address_dfps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['net_address_dfps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecurityPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_codes":
            obj.get("access_codes"),
            "created_time":
            obj.get("created_time"),
            "default_action":
            obj.get("default_action"),
            "default_redirect_name":
            obj.get("default_redirect_name"),
            "description":
            obj.get("description"),
            "dfp_services":
            obj.get("dfp_services"),
            "dfps":
            obj.get("dfps"),
            "ecs":
            obj.get("ecs"),
            "id":
            obj.get("id"),
            "is_default":
            obj.get("is_default"),
            "name":
            obj.get("name"),
            "net_address_dfps": [
                NetAddrDfpAssignment.from_dict(_item)
                for _item in obj["net_address_dfps"]
            ] if obj.get("net_address_dfps") is not None else None,
            "network_lists":
            obj.get("network_lists"),
            "onprem_resolve":
            obj.get("onprem_resolve"),
            "precedence":
            obj.get("precedence"),
            "roaming_device_groups":
            obj.get("roaming_device_groups"),
            "rules":
            [SecurityPolicyRule.from_dict(_item) for _item in obj["rules"]]
            if obj.get("rules") is not None else None,
            "safe_search":
            obj.get("safe_search"),
            "tags":
            obj.get("tags"),
            "updated_time":
            obj.get("updated_time"),
            "user_groups":
            obj.get("user_groups")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
