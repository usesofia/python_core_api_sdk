# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class UserRelatedWorkspaceEntity(BaseModel):
    """
    UserRelatedWorkspaceEntity
    """ # noqa: E501
    id: StrictStr
    pretty_id: StrictStr = Field(alias="prettyId")
    name: StrictStr
    type: StrictStr
    creator_user_id: StrictStr = Field(alias="creatorUserId")
    created_at: datetime = Field(alias="createdAt")
    relation_type: StrictStr = Field(alias="relationType")
    __properties: ClassVar[List[str]] = ["id", "prettyId", "name", "type", "creatorUserId", "createdAt", "relationType"]

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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserRelatedWorkspaceEntity from a dict"""
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
            "createdAt": obj.get("createdAt"),
            "relationType": obj.get("relationType")
        })
        return _obj


