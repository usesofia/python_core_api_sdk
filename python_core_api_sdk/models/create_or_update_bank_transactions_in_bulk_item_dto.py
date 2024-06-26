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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from python_core_api_sdk.models.category_guess_dto import CategoryGuessDto
from python_core_api_sdk.models.credit_card_metadata_dto import CreditCardMetadataDto
from python_core_api_sdk.models.payment_data_dto import PaymentDataDto
from typing import Optional, Set
from typing_extensions import Self

class CreateOrUpdateBankTransactionsInBulkItemDto(BaseModel):
    """
    CreateOrUpdateBankTransactionsInBulkItemDto
    """ # noqa: E501
    account_id: StrictStr = Field(alias="accountId")
    provider: StrictStr
    workspace_id: StrictStr = Field(alias="workspaceId")
    provider_transaction_id: StrictStr = Field(alias="providerTransactionId")
    description: StrictStr
    posted_date: datetime = Field(alias="postedDate")
    competency_date: datetime = Field(alias="competencyDate")
    amount: Union[StrictFloat, StrictInt]
    type: StrictStr
    status: StrictStr
    legal_nature: StrictStr = Field(alias="legalNature")
    provider_category_id: Optional[StrictStr] = Field(default=None, alias="providerCategoryId")
    provider_category_name: Optional[StrictStr] = Field(default=None, alias="providerCategoryName")
    category_id: StrictStr = Field(alias="categoryId")
    payment_data: PaymentDataDto = Field(alias="paymentData")
    credit_card_metadata: CreditCardMetadataDto = Field(alias="creditCardMetadata")
    category_guesses: Optional[List[CategoryGuessDto]] = Field(default=None, alias="categoryGuesses")
    best_guess_category_id: StrictStr = Field(alias="bestGuessCategoryId")
    __properties: ClassVar[List[str]] = ["accountId", "provider", "workspaceId", "providerTransactionId", "description", "postedDate", "competencyDate", "amount", "type", "status", "legalNature", "providerCategoryId", "providerCategoryName", "categoryId", "paymentData", "creditCardMetadata", "categoryGuesses", "bestGuessCategoryId"]

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
        """Create an instance of CreateOrUpdateBankTransactionsInBulkItemDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrUpdateBankTransactionsInBulkItemDto from a dict"""
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
            "type": obj.get("type"),
            "status": obj.get("status"),
            "legalNature": obj.get("legalNature"),
            "providerCategoryId": obj.get("providerCategoryId"),
            "providerCategoryName": obj.get("providerCategoryName"),
            "categoryId": obj.get("categoryId"),
            "paymentData": PaymentDataDto.from_dict(obj["paymentData"]) if obj.get("paymentData") is not None else None,
            "creditCardMetadata": CreditCardMetadataDto.from_dict(obj["creditCardMetadata"]) if obj.get("creditCardMetadata") is not None else None,
            "categoryGuesses": [CategoryGuessDto.from_dict(_item) for _item in obj["categoryGuesses"]] if obj.get("categoryGuesses") is not None else None,
            "bestGuessCategoryId": obj.get("bestGuessCategoryId")
        })
        return _obj


