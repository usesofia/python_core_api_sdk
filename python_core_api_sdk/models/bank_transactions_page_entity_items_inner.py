# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.bank_transaction_entity_account import BankTransactionEntityAccount
from python_core_api_sdk.models.bank_transaction_entity_category import BankTransactionEntityCategory
from python_core_api_sdk.models.bank_transaction_entity_credit_card_metadata import BankTransactionEntityCreditCardMetadata
from python_core_api_sdk.models.bank_transaction_entity_payment_data import BankTransactionEntityPaymentData
from python_core_api_sdk.models.bank_transaction_entity_tags_inner import BankTransactionEntityTagsInner
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionsPageEntityItemsInner(BaseModel):
    """
    BankTransactionsPageEntityItemsInner
    """ # noqa: E501
    id: StrictStr
    account_id: StrictStr = Field(alias="accountId")
    account: BankTransactionEntityAccount
    workspace_id: StrictStr = Field(alias="workspaceId")
    provider: StrictStr
    provider_transaction_id: StrictStr = Field(alias="providerTransactionId")
    original_description: StrictStr = Field(alias="originalDescription")
    description: StrictStr
    posted_date: datetime = Field(alias="postedDate")
    competency_date: datetime = Field(alias="competencyDate")
    amount: StrictInt
    direction_nature: StrictStr = Field(alias="directionNature")
    status: StrictStr
    legal_nature: StrictStr = Field(alias="legalNature")
    provider_category_id: Optional[StrictStr] = Field(default=None, alias="providerCategoryId")
    provider_category_name: Optional[StrictStr] = Field(default=None, alias="providerCategoryName")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category: Optional[BankTransactionEntityCategory] = None
    tags: List[BankTransactionEntityTagsInner]
    payment_data_id: Optional[StrictStr] = Field(default=None, alias="paymentDataId")
    payment_data: Optional[BankTransactionEntityPaymentData] = Field(default=None, alias="paymentData")
    credit_card_metadata_id: Optional[StrictStr] = Field(default=None, alias="creditCardMetadataId")
    credit_card_metadata: Optional[BankTransactionEntityCreditCardMetadata] = Field(default=None, alias="creditCardMetadata")
    ignored_at: Optional[datetime] = Field(default=None, alias="ignoredAt")
    verified_at: Optional[datetime] = Field(default=None, alias="verifiedAt")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "accountId", "account", "workspaceId", "provider", "providerTransactionId", "originalDescription", "description", "postedDate", "competencyDate", "amount", "directionNature", "status", "legalNature", "providerCategoryId", "providerCategoryName", "categoryId", "category", "tags", "paymentDataId", "paymentData", "creditCardMetadataId", "creditCardMetadata", "ignoredAt", "verifiedAt", "createdAt", "updatedAt"]

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
        """Create an instance of BankTransactionsPageEntityItemsInner from a JSON string"""
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
        # set to None if provider_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.provider_category_id is None and "provider_category_id" in self.model_fields_set:
            _dict['providerCategoryId'] = None

        # set to None if provider_category_name (nullable) is None
        # and model_fields_set contains the field
        if self.provider_category_name is None and "provider_category_name" in self.model_fields_set:
            _dict['providerCategoryName'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['categoryId'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if payment_data_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_data_id is None and "payment_data_id" in self.model_fields_set:
            _dict['paymentDataId'] = None

        # set to None if payment_data (nullable) is None
        # and model_fields_set contains the field
        if self.payment_data is None and "payment_data" in self.model_fields_set:
            _dict['paymentData'] = None

        # set to None if credit_card_metadata_id (nullable) is None
        # and model_fields_set contains the field
        if self.credit_card_metadata_id is None and "credit_card_metadata_id" in self.model_fields_set:
            _dict['creditCardMetadataId'] = None

        # set to None if credit_card_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.credit_card_metadata is None and "credit_card_metadata" in self.model_fields_set:
            _dict['creditCardMetadata'] = None

        # set to None if ignored_at (nullable) is None
        # and model_fields_set contains the field
        if self.ignored_at is None and "ignored_at" in self.model_fields_set:
            _dict['ignoredAt'] = None

        # set to None if verified_at (nullable) is None
        # and model_fields_set contains the field
        if self.verified_at is None and "verified_at" in self.model_fields_set:
            _dict['verifiedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransactionsPageEntityItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "account": BankTransactionEntityAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "workspaceId": obj.get("workspaceId"),
            "provider": obj.get("provider"),
            "providerTransactionId": obj.get("providerTransactionId"),
            "originalDescription": obj.get("originalDescription"),
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
            "category": BankTransactionEntityCategory.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "tags": [BankTransactionEntityTagsInner.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "paymentDataId": obj.get("paymentDataId"),
            "paymentData": BankTransactionEntityPaymentData.from_dict(obj["paymentData"]) if obj.get("paymentData") is not None else None,
            "creditCardMetadataId": obj.get("creditCardMetadataId"),
            "creditCardMetadata": BankTransactionEntityCreditCardMetadata.from_dict(obj["creditCardMetadata"]) if obj.get("creditCardMetadata") is not None else None,
            "ignoredAt": obj.get("ignoredAt"),
            "verifiedAt": obj.get("verifiedAt"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


