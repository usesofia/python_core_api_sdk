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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from python_core_api_sdk.models.user_entity_workspaces_inner_hybrid_settings import UserEntityWorkspacesInnerHybridSettings
from python_core_api_sdk.models.user_entity_workspaces_inner_personal_settings import UserEntityWorkspacesInnerPersonalSettings
from typing import Optional, Set
from typing_extensions import Self

class MessageTokenEntityWorksapce(BaseModel):
    """
    MessageTokenEntityWorksapce
    """ # noqa: E501
    id: StrictStr
    pretty_id: Annotated[str, Field(min_length=1, strict=True, max_length=256)] = Field(alias="prettyId")
    name: Annotated[str, Field(min_length=1, strict=True)]
    type: StrictStr
    creator_user_id: StrictStr = Field(alias="creatorUserId")
    selected_personal_category_tree_id: Optional[StrictStr] = Field(default=None, alias="selectedPersonalCategoryTreeId")
    selected_business_category_tree_id: Optional[StrictStr] = Field(default=None, alias="selectedBusinessCategoryTreeId")
    hybrid_settings: Optional[UserEntityWorkspacesInnerHybridSettings] = Field(default=None, alias="hybridSettings")
    business_settings: Optional[UserEntityWorkspacesInnerHybridSettings] = Field(default=None, alias="businessSettings")
    personal_settings: Optional[UserEntityWorkspacesInnerPersonalSettings] = Field(default=None, alias="personalSettings")
    created_at: datetime = Field(alias="createdAt")
    __properties: ClassVar[List[str]] = ["id", "prettyId", "name", "type", "creatorUserId", "selectedPersonalCategoryTreeId", "selectedBusinessCategoryTreeId", "hybridSettings", "businessSettings", "personalSettings", "createdAt"]

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
        """Create an instance of MessageTokenEntityWorksapce from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hybrid_settings
        if self.hybrid_settings:
            _dict['hybridSettings'] = self.hybrid_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_settings
        if self.business_settings:
            _dict['businessSettings'] = self.business_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of personal_settings
        if self.personal_settings:
            _dict['personalSettings'] = self.personal_settings.to_dict()
        # set to None if selected_personal_category_tree_id (nullable) is None
        # and model_fields_set contains the field
        if self.selected_personal_category_tree_id is None and "selected_personal_category_tree_id" in self.model_fields_set:
            _dict['selectedPersonalCategoryTreeId'] = None

        # set to None if selected_business_category_tree_id (nullable) is None
        # and model_fields_set contains the field
        if self.selected_business_category_tree_id is None and "selected_business_category_tree_id" in self.model_fields_set:
            _dict['selectedBusinessCategoryTreeId'] = None

        # set to None if hybrid_settings (nullable) is None
        # and model_fields_set contains the field
        if self.hybrid_settings is None and "hybrid_settings" in self.model_fields_set:
            _dict['hybridSettings'] = None

        # set to None if business_settings (nullable) is None
        # and model_fields_set contains the field
        if self.business_settings is None and "business_settings" in self.model_fields_set:
            _dict['businessSettings'] = None

        # set to None if personal_settings (nullable) is None
        # and model_fields_set contains the field
        if self.personal_settings is None and "personal_settings" in self.model_fields_set:
            _dict['personalSettings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageTokenEntityWorksapce from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "prettyId": obj.get("prettyId"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "creatorUserId": obj.get("creatorUserId"),
            "selectedPersonalCategoryTreeId": obj.get("selectedPersonalCategoryTreeId"),
            "selectedBusinessCategoryTreeId": obj.get("selectedBusinessCategoryTreeId"),
            "hybridSettings": UserEntityWorkspacesInnerHybridSettings.from_dict(obj["hybridSettings"]) if obj.get("hybridSettings") is not None else None,
            "businessSettings": UserEntityWorkspacesInnerHybridSettings.from_dict(obj["businessSettings"]) if obj.get("businessSettings") is not None else None,
            "personalSettings": UserEntityWorkspacesInnerPersonalSettings.from_dict(obj["personalSettings"]) if obj.get("personalSettings") is not None else None,
            "createdAt": obj.get("createdAt")
        })
        return _obj


