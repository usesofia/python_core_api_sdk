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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionCreditCardMetadataEntity(BaseModel):
    """
    BankTransactionCreditCardMetadataEntity
    """ # noqa: E501
    id: StrictStr
    transaction_id: StrictStr = Field(alias="transactionId")
    installment_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="installmentNumber")
    total_installments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalInstallments")
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalAmount")
    payee_mcc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="payeeMCC")
    card_number: Optional[StrictStr] = Field(default=None, alias="cardNumber")
    bill_id: Optional[StrictStr] = Field(default=None, alias="billId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "transactionId", "installmentNumber", "totalInstallments", "totalAmount", "payeeMCC", "cardNumber", "billId", "createdAt", "updatedAt"]

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
        """Create an instance of BankTransactionCreditCardMetadataEntity from a JSON string"""
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
        """Create an instance of BankTransactionCreditCardMetadataEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "transactionId": obj.get("transactionId"),
            "installmentNumber": obj.get("installmentNumber"),
            "totalInstallments": obj.get("totalInstallments"),
            "totalAmount": obj.get("totalAmount"),
            "payeeMCC": obj.get("payeeMCC"),
            "cardNumber": obj.get("cardNumber"),
            "billId": obj.get("billId"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


