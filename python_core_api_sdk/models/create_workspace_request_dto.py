# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CreateWorkspaceRequestDto(BaseModel):
    """
    CreateWorkspaceRequestDto
    """ # noqa: E501
    pretty_id: Annotated[str, Field(min_length=1, strict=True, max_length=256)] = Field(alias="prettyId")
    name: Annotated[str, Field(min_length=1, strict=True)]
    type: StrictStr
    business_segment: Optional[StrictStr] = Field(default=None, alias="businessSegment")
    other_description: Optional[StrictStr] = Field(default=None, alias="otherDescription")
    throw_after_create_workspace: Optional[StrictBool] = Field(default=None, alias="throwAfterCreateWorkspace")
    __properties: ClassVar[List[str]] = ["prettyId", "name", "type", "businessSegment", "otherDescription", "throwAfterCreateWorkspace"]

    @field_validator('pretty_id')
    def pretty_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z0-9-]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z0-9-]+$/")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PERSONAL', 'BUSINESS', 'HYBRID']):
            raise ValueError("must be one of enum values ('PERSONAL', 'BUSINESS', 'HYBRID')")
        return value

    @field_validator('business_segment')
    def business_segment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        """Create an instance of CreateWorkspaceRequestDto from a JSON string"""
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
        # set to None if business_segment (nullable) is None
        # and model_fields_set contains the field
        if self.business_segment is None and "business_segment" in self.model_fields_set:
            _dict['businessSegment'] = None

        # set to None if other_description (nullable) is None
        # and model_fields_set contains the field
        if self.other_description is None and "other_description" in self.model_fields_set:
            _dict['otherDescription'] = None

        # set to None if throw_after_create_workspace (nullable) is None
        # and model_fields_set contains the field
        if self.throw_after_create_workspace is None and "throw_after_create_workspace" in self.model_fields_set:
            _dict['throwAfterCreateWorkspace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateWorkspaceRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prettyId": obj.get("prettyId"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "businessSegment": obj.get("businessSegment"),
            "otherDescription": obj.get("otherDescription"),
            "throwAfterCreateWorkspace": obj.get("throwAfterCreateWorkspace")
        })
        return _obj


