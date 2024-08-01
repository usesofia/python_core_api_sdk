# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from python_core_api_sdk.models.user_entity_workspaces_inner import UserEntityWorkspacesInner
from typing import Optional, Set
from typing_extensions import Self

class UserRelatedWorkspaceEntity(BaseModel):
    """
    UserRelatedWorkspaceEntity
    """ # noqa: E501
    workspace: UserEntityWorkspacesInner
    relation_type: StrictStr = Field(alias="relationType")
    __properties: ClassVar[List[str]] = ["workspace", "relationType"]

    @field_validator('relation_type')
    def relation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['APPROVED', 'WAITING_APPROVAL']):
            raise ValueError("must be one of enum values ('APPROVED', 'WAITING_APPROVAL')")
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
        """Create an instance of UserRelatedWorkspaceEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workspace
        if self.workspace:
            _dict['workspace'] = self.workspace.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserRelatedWorkspaceEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace": UserEntityWorkspacesInner.from_dict(obj["workspace"]) if obj.get("workspace") is not None else None,
            "relationType": obj.get("relationType")
        })
        return _obj


