# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dns_config.models.external_primary import ExternalPrimary
from dns_config.models.external_secondary import ExternalSecondary
from dns_config.models.internal_secondary import InternalSecondary
from typing import Optional, Set
from typing_extensions import Self

class CopyAuthZone(BaseModel):
    """
    CopyAuthZone
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="A comment of the (copied) _dns/auth_zone_ object.")
    external_primaries: Optional[List[ExternalPrimary]] = Field(default=None, description="DNS primaries external to BloxOne DDI. Order is not significant.")
    external_secondaries: Optional[List[ExternalSecondary]] = Field(default=None, description="DNS secondaries external to BloxOne DDI. Order is not significant.")
    id: Optional[StrictStr] = Field(default=None, description="The resource identifier.")
    internal_secondaries: Optional[List[InternalSecondary]] = Field(default=None, description="BloxOne DDI hosts acting as internal secondaries. Order is not significant.")
    nsgs: Optional[List[StrictStr]] = Field(default=None, description="The resource identifier.")
    recursive: Optional[StrictBool] = Field(default=None, description="Indicates whether child objects should be copied or not.  Defaults to _false_. Reserved for future use.")
    skip_on_error: Optional[StrictBool] = Field(default=None, description="Indicates whether copying should skip object in case of error and continue with next, or abort copying in case of error.  Defaults to _false_.")
    target_view: StrictStr = Field(description="The resource identifier.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["comment", "external_primaries", "external_secondaries", "id", "internal_secondaries", "nsgs", "recursive", "skip_on_error", "target_view"]

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
        """Create an instance of CopyAuthZone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in external_primaries (list)
        _items = []
        if self.external_primaries:
            for _item in self.external_primaries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['external_primaries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_secondaries (list)
        _items = []
        if self.external_secondaries:
            for _item in self.external_secondaries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['external_secondaries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in internal_secondaries (list)
        _items = []
        if self.internal_secondaries:
            for _item in self.internal_secondaries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['internal_secondaries'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CopyAuthZone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "external_primaries": [ExternalPrimary.from_dict(_item) for _item in obj["external_primaries"]] if obj.get("external_primaries") is not None else None,
            "external_secondaries": [ExternalSecondary.from_dict(_item) for _item in obj["external_secondaries"]] if obj.get("external_secondaries") is not None else None,
            "id": obj.get("id"),
            "internal_secondaries": [InternalSecondary.from_dict(_item) for _item in obj["internal_secondaries"]] if obj.get("internal_secondaries") is not None else None,
            "nsgs": obj.get("nsgs"),
            "recursive": obj.get("recursive"),
            "skip_on_error": obj.get("skip_on_error"),
            "target_view": obj.get("target_view")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

