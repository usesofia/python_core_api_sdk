# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.user_entity_workspaces_inner import UserEntityWorkspacesInner
from typing import Optional, Set
from typing_extensions import Self

class UserEntity(BaseModel):
    """
    UserEntity
    """ # noqa: E501
    id: StrictStr
    email: StrictStr
    phone: StrictStr
    password_hash: Optional[StrictStr] = Field(default=None, alias="passwordHash")
    is_root: StrictBool = Field(alias="isRoot")
    workspaces: Optional[List[UserEntityWorkspacesInner]] = None
    created_at: datetime = Field(alias="createdAt")
    __properties: ClassVar[List[str]] = ["id", "email", "phone", "passwordHash", "isRoot", "workspaces", "createdAt"]

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
        """Create an instance of UserEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in workspaces (list)
        _items = []
        if self.workspaces:
            for _item in self.workspaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workspaces'] = _items
        # set to None if password_hash (nullable) is None
        # and model_fields_set contains the field
        if self.password_hash is None and "password_hash" in self.model_fields_set:
            _dict['passwordHash'] = None

        # set to None if workspaces (nullable) is None
        # and model_fields_set contains the field
        if self.workspaces is None and "workspaces" in self.model_fields_set:
            _dict['workspaces'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "passwordHash": obj.get("passwordHash"),
            "isRoot": obj.get("isRoot"),
            "workspaces": [UserEntityWorkspacesInner.from_dict(_item) for _item in obj["workspaces"]] if obj.get("workspaces") is not None else None,
            "createdAt": obj.get("createdAt")
        })
        return _obj


