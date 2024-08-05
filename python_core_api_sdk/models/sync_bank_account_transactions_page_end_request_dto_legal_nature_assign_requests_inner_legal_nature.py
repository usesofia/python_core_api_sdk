# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_legal_nature_guesses_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner
from typing import Optional, Set
from typing_extensions import Self

class SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature(BaseModel):
    """
    SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature
    """ # noqa: E501
    origin: StrictStr
    value: StrictStr
    prediction_response: Optional[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner] = Field(default=None, alias="predictionResponse")
    __properties: ClassVar[List[str]] = ["origin", "value", "predictionResponse"]

    @field_validator('origin')
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AUTOMATIC', 'PREDICTION']):
            raise ValueError("must be one of enum values ('AUTOMATIC', 'PREDICTION')")
        return value

    @field_validator('value')
    def value_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PERSONAL', 'BUSINESS', 'UNDEFINED']):
            raise ValueError("must be one of enum values ('PERSONAL', 'BUSINESS', 'UNDEFINED')")
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
        """Create an instance of SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of prediction_response
        if self.prediction_response:
            _dict['predictionResponse'] = self.prediction_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "origin": obj.get("origin"),
            "value": obj.get("value"),
            "predictionResponse": CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner.from_dict(obj["predictionResponse"]) if obj.get("predictionResponse") is not None else None
        })
        return _obj


