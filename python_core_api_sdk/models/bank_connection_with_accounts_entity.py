# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from python_core_api_sdk.models.bank_connector_entity import BankConnectorEntity
from python_core_api_sdk.models.plain_bank_account_entity import PlainBankAccountEntity
from typing import Optional, Set
from typing_extensions import Self

class BankConnectionWithAccountsEntity(BaseModel):
    """
    BankConnectionWithAccountsEntity
    """ # noqa: E501
    id: StrictStr
    created_by_user_id: StrictStr = Field(alias="createdByUserId")
    workspace_id: StrictStr = Field(alias="workspaceId")
    accounts: List[PlainBankAccountEntity]
    enabled: StrictBool
    provider: StrictStr
    provider_item_id: StrictStr = Field(alias="providerItemId")
    history_range: StrictStr = Field(alias="historyRange")
    connector_id: StrictStr = Field(alias="connectorId")
    connector: BankConnectorEntity
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "createdByUserId", "workspaceId", "accounts", "enabled", "provider", "providerItemId", "historyRange", "connectorId", "connector", "createdAt", "updatedAt"]

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
        """Create an instance of BankConnectionWithAccountsEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item in self.accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankConnectionWithAccountsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdByUserId": obj.get("createdByUserId"),
            "workspaceId": obj.get("workspaceId"),
            "accounts": [PlainBankAccountEntity.from_dict(_item) for _item in obj["accounts"]] if obj.get("accounts") is not None else None,
            "enabled": obj.get("enabled"),
            "provider": obj.get("provider"),
            "providerItemId": obj.get("providerItemId"),
            "historyRange": obj.get("historyRange"),
            "connectorId": obj.get("connectorId"),
            "connector": BankConnectorEntity.from_dict(obj["connector"]) if obj.get("connector") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


