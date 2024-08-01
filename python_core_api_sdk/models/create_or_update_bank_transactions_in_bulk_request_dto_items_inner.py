# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_category_guesses_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_legal_nature_guesses_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData
from typing import Optional, Set
from typing_extensions import Self

class CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner(BaseModel):
    """
    CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner
    """ # noqa: E501
    account_id: StrictStr = Field(alias="accountId")
    provider: StrictStr
    workspace_id: StrictStr = Field(alias="workspaceId")
    provider_transaction_id: StrictStr = Field(alias="providerTransactionId")
    description: StrictStr
    posted_date: Optional[Any] = Field(alias="postedDate")
    competency_date: Optional[Any] = Field(alias="competencyDate")
    amount: Union[StrictFloat, StrictInt]
    direction_nature: StrictStr = Field(alias="directionNature")
    status: StrictStr
    legal_nature: StrictStr = Field(alias="legalNature")
    provider_category_id: Optional[StrictStr] = Field(default=None, alias="providerCategoryId")
    provider_category_name: Optional[StrictStr] = Field(default=None, alias="providerCategoryName")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    payment_data: Optional[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData] = Field(default=None, alias="paymentData")
    credit_card_metadata: Optional[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata] = Field(default=None, alias="creditCardMetadata")
    category_guesses: Optional[List[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner]] = Field(default=None, alias="categoryGuesses")
    legal_nature_guesses: Optional[List[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner]] = Field(default=None, alias="legalNatureGuesses")
    __properties: ClassVar[List[str]] = ["accountId", "provider", "workspaceId", "providerTransactionId", "description", "postedDate", "competencyDate", "amount", "directionNature", "status", "legalNature", "providerCategoryId", "providerCategoryName", "categoryId", "paymentData", "creditCardMetadata", "categoryGuesses", "legalNatureGuesses"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PLUGGY', 'SOFIA']):
            raise ValueError("must be one of enum values ('PLUGGY', 'SOFIA')")
        return value

    @field_validator('direction_nature')
    def direction_nature_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CREDIT', 'DEBIT', 'UNDEFINED']):
            raise ValueError("must be one of enum values ('CREDIT', 'DEBIT', 'UNDEFINED')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PENDING', 'POSTED']):
            raise ValueError("must be one of enum values ('PENDING', 'POSTED')")
        return value

    @field_validator('legal_nature')
    def legal_nature_validate_enum(cls, value):
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
        """Create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_data
        if self.payment_data:
            _dict['paymentData'] = self.payment_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_card_metadata
        if self.credit_card_metadata:
            _dict['creditCardMetadata'] = self.credit_card_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in category_guesses (list)
        _items = []
        if self.category_guesses:
            for _item in self.category_guesses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categoryGuesses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in legal_nature_guesses (list)
        _items = []
        if self.legal_nature_guesses:
            for _item in self.legal_nature_guesses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['legalNatureGuesses'] = _items
        # set to None if posted_date (nullable) is None
        # and model_fields_set contains the field
        if self.posted_date is None and "posted_date" in self.model_fields_set:
            _dict['postedDate'] = None

        # set to None if competency_date (nullable) is None
        # and model_fields_set contains the field
        if self.competency_date is None and "competency_date" in self.model_fields_set:
            _dict['competencyDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "provider": obj.get("provider"),
            "workspaceId": obj.get("workspaceId"),
            "providerTransactionId": obj.get("providerTransactionId"),
            "description": obj.get("description"),
            "postedDate": obj.get("postedDate"),
            "competencyDate": obj.get("competencyDate"),
            "amount": obj.get("amount"),
            "directionNature": obj.get("directionNature"),
            "status": obj.get("status"),
            "legalNature": obj.get("legalNature"),
            "providerCategoryId": obj.get("providerCategoryId"),
            "providerCategoryName": obj.get("providerCategoryName"),
            "categoryId": obj.get("categoryId"),
            "paymentData": CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.from_dict(obj["paymentData"]) if obj.get("paymentData") is not None else None,
            "creditCardMetadata": CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.from_dict(obj["creditCardMetadata"]) if obj.get("creditCardMetadata") is not None else None,
            "categoryGuesses": [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner.from_dict(_item) for _item in obj["categoryGuesses"]] if obj.get("categoryGuesses") is not None else None,
            "legalNatureGuesses": [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner.from_dict(_item) for _item in obj["legalNatureGuesses"]] if obj.get("legalNatureGuesses") is not None else None
        })
        return _obj


