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
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UserEntityWorkspacesInnerHybridSettings(BaseModel):
    """
    UserEntityWorkspacesInnerHybridSettings
    """ # noqa: E501
    id: StrictStr
    business_segment: StrictStr = Field(alias="businessSegment")
    other_business_description: Optional[StrictStr] = Field(default=None, alias="otherBusinessDescription")
    __properties: ClassVar[List[str]] = ["id", "businessSegment", "otherBusinessDescription"]

    @field_validator('business_segment')
    def business_segment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ATTORNEY', 'ARCHITECT', 'CONSULTANT', 'REALTOR', 'INSURANCE_BROKER', 'DENTIST', 'PHYSIOTHERAPIST', 'PHYSICIAN', 'TUTOR', 'PSYCHOLOGIST', 'OTHER']):
            raise ValueError("must be one of enum values ('ATTORNEY', 'ARCHITECT', 'CONSULTANT', 'REALTOR', 'INSURANCE_BROKER', 'DENTIST', 'PHYSIOTHERAPIST', 'PHYSICIAN', 'TUTOR', 'PSYCHOLOGIST', 'OTHER')")
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
        """Create an instance of UserEntityWorkspacesInnerHybridSettings from a JSON string"""
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
        # set to None if other_business_description (nullable) is None
        # and model_fields_set contains the field
        if self.other_business_description is None and "other_business_description" in self.model_fields_set:
            _dict['otherBusinessDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserEntityWorkspacesInnerHybridSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "businessSegment": obj.get("businessSegment"),
            "otherBusinessDescription": obj.get("otherBusinessDescription")
        })
        return _obj


