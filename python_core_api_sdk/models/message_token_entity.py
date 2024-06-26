# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
from typing import Optional, Set
from typing_extensions import Self

class MessageTokenEntity(BaseModel):
    """
    MessageTokenEntity
    """ # noqa: E501
    id: StrictStr
    workspace_id: StrictStr = Field(alias="workspaceId")
    workspace: WorkspaceEntity
    user_id: StrictStr = Field(alias="userId")
    user: UserEntity
    provider: StrictStr
    platform: StrictStr
    device_id: StrictStr = Field(alias="deviceId")
    token: StrictStr
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "workspaceId", "workspace", "userId", "user", "provider", "platform", "deviceId", "token", "createdAt", "updatedAt"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FIREBASE_MESSAGING']):
            raise ValueError("must be one of enum values ('FIREBASE_MESSAGING')")
        return value

    @field_validator('platform')
    def platform_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['WEB', 'ANDROID', 'IOS']):
            raise ValueError("must be one of enum values ('WEB', 'ANDROID', 'IOS')")
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
        """Create an instance of MessageTokenEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageTokenEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "workspaceId": obj.get("workspaceId"),
            "workspace": WorkspaceEntity.from_dict(obj["workspace"]) if obj.get("workspace") is not None else None,
            "userId": obj.get("userId"),
            "user": UserEntity.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "provider": obj.get("provider"),
            "platform": obj.get("platform"),
            "deviceId": obj.get("deviceId"),
            "token": obj.get("token"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


