# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.10
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.bank_connection_entity_connector import BankConnectionEntityConnector
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionEntityAccountBankConnection(BaseModel):
    """
    BankTransactionEntityAccountBankConnection
    """ # noqa: E501
    id: StrictStr
    created_by_user_id: StrictStr = Field(alias="createdByUserId")
    workspace_id: StrictStr = Field(alias="workspaceId")
    enabled: StrictBool
    provider: StrictStr
    provider_item_id: StrictStr = Field(alias="providerItemId")
    history_range: StrictStr = Field(alias="historyRange")
    connector_id: StrictStr = Field(alias="connectorId")
    connector: Optional[BankConnectionEntityConnector] = None
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "createdByUserId", "workspaceId", "enabled", "provider", "providerItemId", "historyRange", "connectorId", "connector", "createdAt", "updatedAt"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PLUGGY', 'SOFIA']):
            raise ValueError("must be one of enum values ('PLUGGY', 'SOFIA')")
        return value

    @field_validator('history_range')
    def history_range_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ONE_DAY', 'ONE_WEEK', 'ONE_MONTH', 'TWO_MONTHS', 'THREE_MONTHS', 'SIX_MONTHS', 'ONE_YEAR']):
            raise ValueError("must be one of enum values ('ONE_DAY', 'ONE_WEEK', 'ONE_MONTH', 'TWO_MONTHS', 'THREE_MONTHS', 'SIX_MONTHS', 'ONE_YEAR')")
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
        """Create an instance of BankTransactionEntityAccountBankConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        # set to None if connector (nullable) is None
        # and model_fields_set contains the field
        if self.connector is None and "connector" in self.model_fields_set:
            _dict['connector'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransactionEntityAccountBankConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdByUserId": obj.get("createdByUserId"),
            "workspaceId": obj.get("workspaceId"),
            "enabled": obj.get("enabled"),
            "provider": obj.get("provider"),
            "providerItemId": obj.get("providerItemId"),
            "historyRange": obj.get("historyRange"),
            "connectorId": obj.get("connectorId"),
            "connector": BankConnectionEntityConnector.from_dict(obj["connector"]) if obj.get("connector") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


