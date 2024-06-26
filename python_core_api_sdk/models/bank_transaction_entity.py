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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.bank_transaction_category_plain_entity import BankTransactionCategoryPlainEntity
from python_core_api_sdk.models.bank_transaction_credit_card_metadata_entity import BankTransactionCreditCardMetadataEntity
from python_core_api_sdk.models.bank_transaction_payment_data_entity import BankTransactionPaymentDataEntity
from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionEntity(BaseModel):
    """
    BankTransactionEntity
    """ # noqa: E501
    id: StrictStr
    account_id: StrictStr = Field(alias="accountId")
    account: BankAccountEntity
    workspace_id: StrictStr = Field(alias="workspaceId")
    provider: StrictStr
    provider_transaction_id: StrictStr = Field(alias="providerTransactionId")
    original_description: StrictStr = Field(alias="originalDescription")
    description: StrictStr
    posted_date: datetime = Field(alias="postedDate")
    competency_date: datetime = Field(alias="competencyDate")
    amount: Union[StrictFloat, StrictInt]
    type: StrictStr
    status: StrictStr
    legal_nature: StrictStr = Field(alias="legalNature")
    provider_category_id: Optional[StrictStr] = Field(default=None, alias="providerCategoryId")
    provider_category_name: Optional[StrictStr] = Field(default=None, alias="providerCategoryName")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category: Optional[BankTransactionCategoryPlainEntity] = None
    tags: List[BankTransactionTagEntity]
    payment_data_id: Optional[StrictStr] = Field(default=None, alias="paymentDataId")
    payment_data: Optional[BankTransactionPaymentDataEntity] = Field(default=None, alias="paymentData")
    credit_card_metadata_id: Optional[StrictStr] = Field(default=None, alias="creditCardMetadataId")
    credit_card_metadata: Optional[BankTransactionCreditCardMetadataEntity] = Field(default=None, alias="creditCardMetadata")
    best_guess_category_id: Optional[StrictStr] = Field(default=None, alias="bestGuessCategoryId")
    best_guess_category: Optional[BankTransactionCategoryPlainEntity] = Field(default=None, alias="bestGuessCategory")
    ignored_at: Optional[datetime] = Field(default=None, alias="ignoredAt")
    confirmed_at: Optional[datetime] = Field(default=None, alias="confirmedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "accountId", "account", "workspaceId", "provider", "providerTransactionId", "originalDescription", "description", "postedDate", "competencyDate", "amount", "type", "status", "legalNature", "providerCategoryId", "providerCategoryName", "categoryId", "category", "tags", "paymentDataId", "paymentData", "creditCardMetadataId", "creditCardMetadata", "bestGuessCategoryId", "bestGuessCategory", "ignoredAt", "confirmedAt", "createdAt", "updatedAt"]

    @field_validator('provider')
    def provider_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PLUGGY', 'SOFIA']):
            raise ValueError("must be one of enum values ('PLUGGY', 'SOFIA')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DEBIT', 'CREDIT', 'UNDEFINED']):
            raise ValueError("must be one of enum values ('DEBIT', 'CREDIT', 'UNDEFINED')")
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
        if value not in set(['PERSONAL', 'BUSINESS']):
            raise ValueError("must be one of enum values ('PERSONAL', 'BUSINESS')")
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
        """Create an instance of BankTransactionEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_data
        if self.payment_data:
            _dict['paymentData'] = self.payment_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_card_metadata
        if self.credit_card_metadata:
            _dict['creditCardMetadata'] = self.credit_card_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of best_guess_category
        if self.best_guess_category:
            _dict['bestGuessCategory'] = self.best_guess_category.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransactionEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "account": BankAccountEntity.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "workspaceId": obj.get("workspaceId"),
            "provider": obj.get("provider"),
            "providerTransactionId": obj.get("providerTransactionId"),
            "originalDescription": obj.get("originalDescription"),
            "description": obj.get("description"),
            "postedDate": obj.get("postedDate"),
            "competencyDate": obj.get("competencyDate"),
            "amount": obj.get("amount"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "legalNature": obj.get("legalNature"),
            "providerCategoryId": obj.get("providerCategoryId"),
            "providerCategoryName": obj.get("providerCategoryName"),
            "categoryId": obj.get("categoryId"),
            "category": BankTransactionCategoryPlainEntity.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "tags": [BankTransactionTagEntity.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "paymentDataId": obj.get("paymentDataId"),
            "paymentData": BankTransactionPaymentDataEntity.from_dict(obj["paymentData"]) if obj.get("paymentData") is not None else None,
            "creditCardMetadataId": obj.get("creditCardMetadataId"),
            "creditCardMetadata": BankTransactionCreditCardMetadataEntity.from_dict(obj["creditCardMetadata"]) if obj.get("creditCardMetadata") is not None else None,
            "bestGuessCategoryId": obj.get("bestGuessCategoryId"),
            "bestGuessCategory": BankTransactionCategoryPlainEntity.from_dict(obj["bestGuessCategory"]) if obj.get("bestGuessCategory") is not None else None,
            "ignoredAt": obj.get("ignoredAt"),
            "confirmedAt": obj.get("confirmedAt"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


