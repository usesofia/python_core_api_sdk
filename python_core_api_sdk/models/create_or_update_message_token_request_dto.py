# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.11
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CreateOrUpdateMessageTokenRequestDto(BaseModel):
    """
    CreateOrUpdateMessageTokenRequestDto
    """ # noqa: E501
    platform: StrictStr
    provider: StrictStr
    device_id: StrictStr = Field(alias="deviceId")
    token: StrictStr
    __properties: ClassVar[List[str]] = ["platform", "provider", "deviceId", "token"]

    @field_validator('platform')
    def platform_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['WEB', 'ANDROID', 'IOS']):
            raise ValueError("must be one of enum values ('WEB', 'ANDROID', 'IOS')")
        return value

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FIREBASE_MESSAGING']):
            raise ValueError("must be one of enum values ('FIREBASE_MESSAGING')")
        return value

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
        """Create an instance of CreateOrUpdateMessageTokenRequestDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrUpdateMessageTokenRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "platform": obj.get("platform"),
            "provider": obj.get("provider"),
            "deviceId": obj.get("deviceId"),
            "token": obj.get("token")
        })
        return _obj


