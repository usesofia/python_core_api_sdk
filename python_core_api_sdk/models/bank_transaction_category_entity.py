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
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.bank_transaction_category_entity_children_inner import BankTransactionCategoryEntityChildrenInner
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionCategoryEntity(BaseModel):
    """
    BankTransactionCategoryEntity
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    direction_nature: StrictStr = Field(alias="directionNature")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    children: List[BankTransactionCategoryEntityChildrenInner]
    __properties: ClassVar[List[str]] = ["id", "name", "directionNature", "parentId", "children"]

    @field_validator('direction_nature')
    def direction_nature_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CREDIT', 'DEBIT', 'UNDEFINED']):
            raise ValueError("must be one of enum values ('CREDIT', 'DEBIT', 'UNDEFINED')")
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
        """Create an instance of BankTransactionCategoryEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item in self.children:
                if _item:
                    _items.append(_item.to_dict())
            _dict['children'] = _items
        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parentId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransactionCategoryEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "directionNature": obj.get("directionNature"),
            "parentId": obj.get("parentId"),
            "children": [BankTransactionCategoryEntityChildrenInner.from_dict(_item) for _item in obj["children"]] if obj.get("children") is not None else None
        })
        return _obj


