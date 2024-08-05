# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.7
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from python_core_api_sdk.models.bank_transaction_entity_account_bank_connection import BankTransactionEntityAccountBankConnection
from typing import Optional, Set
from typing_extensions import Self

class BankAccountEntity(BaseModel):
    """
    BankAccountEntity
    """ # noqa: E501
    id: StrictStr
    bank_connection_id: StrictStr = Field(alias="bankConnectionId")
    bank_connection: BankTransactionEntityAccountBankConnection = Field(alias="bankConnection")
    provider: StrictStr
    provider_account_id: StrictStr = Field(alias="providerAccountId")
    type: StrictStr
    enabled: StrictBool
    number: StrictStr
    balance: StrictInt
    currency_code: StrictStr = Field(alias="currencyCode")
    name: StrictStr
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "bankConnectionId", "bankConnection", "provider", "providerAccountId", "type", "enabled", "number", "balance", "currencyCode", "name", "createdAt", "updatedAt"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PLUGGY', 'SOFIA']):
            raise ValueError("must be one of enum values ('PLUGGY', 'SOFIA')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CHECKING', 'SAVINGS', 'CREDIT_CARD']):
            raise ValueError("must be one of enum values ('CHECKING', 'SAVINGS', 'CREDIT_CARD')")
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
        """Create an instance of BankAccountEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_connection
        if self.bank_connection:
            _dict['bankConnection'] = self.bank_connection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankAccountEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bankConnectionId": obj.get("bankConnectionId"),
            "bankConnection": BankTransactionEntityAccountBankConnection.from_dict(obj["bankConnection"]) if obj.get("bankConnection") is not None else None,
            "provider": obj.get("provider"),
            "providerAccountId": obj.get("providerAccountId"),
            "type": obj.get("type"),
            "enabled": obj.get("enabled"),
            "number": obj.get("number"),
            "balance": obj.get("balance"),
            "currencyCode": obj.get("currencyCode"),
            "name": obj.get("name"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


