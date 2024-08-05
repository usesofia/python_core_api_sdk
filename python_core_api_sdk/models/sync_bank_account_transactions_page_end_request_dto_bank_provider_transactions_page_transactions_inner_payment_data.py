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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData(BaseModel):
    """
    SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData
    """ # noqa: E501
    payer_name: Optional[StrictStr] = Field(default=None, alias="payerName")
    payer_branch_number: Optional[StrictStr] = Field(default=None, alias="payerBranchNumber")
    payer_account_number: Optional[StrictStr] = Field(default=None, alias="payerAccountNumber")
    payer_routing_number: Optional[StrictStr] = Field(default=None, alias="payerRoutingNumber")
    payer_routing_number_ispb: Optional[StrictStr] = Field(default=None, alias="payerRoutingNumberISPB")
    payer_document_number_type: Optional[StrictStr] = Field(default=None, alias="payerDocumentNumberType")
    payer_document_number_value: Optional[StrictStr] = Field(default=None, alias="payerDocumentNumberValue")
    reason: Optional[StrictStr] = None
    receiver_name: Optional[StrictStr] = Field(default=None, alias="receiverName")
    receiver_branch_number: Optional[StrictStr] = Field(default=None, alias="receiverBranchNumber")
    receiver_account_number: Optional[StrictStr] = Field(default=None, alias="receiverAccountNumber")
    receiver_routing_number: Optional[StrictStr] = Field(default=None, alias="receiverRoutingNumber")
    receiver_routing_number_ispb: Optional[StrictStr] = Field(default=None, alias="receiverRoutingNumberISPB")
    receiver_document_number_type: Optional[StrictStr] = Field(default=None, alias="receiverDocumentNumberType")
    receiver_document_number_value: Optional[StrictStr] = Field(default=None, alias="receiverDocumentNumberValue")
    payment_method: Optional[StrictStr] = Field(default=None, alias="paymentMethod")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    receiver_reference_id: Optional[StrictStr] = Field(default=None, alias="receiverReferenceId")
    __properties: ClassVar[List[str]] = ["payerName", "payerBranchNumber", "payerAccountNumber", "payerRoutingNumber", "payerRoutingNumberISPB", "payerDocumentNumberType", "payerDocumentNumberValue", "reason", "receiverName", "receiverBranchNumber", "receiverAccountNumber", "receiverRoutingNumber", "receiverRoutingNumberISPB", "receiverDocumentNumberType", "receiverDocumentNumberValue", "paymentMethod", "referenceNumber", "receiverReferenceId"]

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
        """Create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData from a JSON string"""
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
        # set to None if payer_name (nullable) is None
        # and model_fields_set contains the field
        if self.payer_name is None and "payer_name" in self.model_fields_set:
            _dict['payerName'] = None

        # set to None if payer_branch_number (nullable) is None
        # and model_fields_set contains the field
        if self.payer_branch_number is None and "payer_branch_number" in self.model_fields_set:
            _dict['payerBranchNumber'] = None

        # set to None if payer_account_number (nullable) is None
        # and model_fields_set contains the field
        if self.payer_account_number is None and "payer_account_number" in self.model_fields_set:
            _dict['payerAccountNumber'] = None

        # set to None if payer_routing_number (nullable) is None
        # and model_fields_set contains the field
        if self.payer_routing_number is None and "payer_routing_number" in self.model_fields_set:
            _dict['payerRoutingNumber'] = None

        # set to None if payer_routing_number_ispb (nullable) is None
        # and model_fields_set contains the field
        if self.payer_routing_number_ispb is None and "payer_routing_number_ispb" in self.model_fields_set:
            _dict['payerRoutingNumberISPB'] = None

        # set to None if payer_document_number_type (nullable) is None
        # and model_fields_set contains the field
        if self.payer_document_number_type is None and "payer_document_number_type" in self.model_fields_set:
            _dict['payerDocumentNumberType'] = None

        # set to None if payer_document_number_value (nullable) is None
        # and model_fields_set contains the field
        if self.payer_document_number_value is None and "payer_document_number_value" in self.model_fields_set:
            _dict['payerDocumentNumberValue'] = None

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if receiver_name (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_name is None and "receiver_name" in self.model_fields_set:
            _dict['receiverName'] = None

        # set to None if receiver_branch_number (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_branch_number is None and "receiver_branch_number" in self.model_fields_set:
            _dict['receiverBranchNumber'] = None

        # set to None if receiver_account_number (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_account_number is None and "receiver_account_number" in self.model_fields_set:
            _dict['receiverAccountNumber'] = None

        # set to None if receiver_routing_number (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_routing_number is None and "receiver_routing_number" in self.model_fields_set:
            _dict['receiverRoutingNumber'] = None

        # set to None if receiver_routing_number_ispb (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_routing_number_ispb is None and "receiver_routing_number_ispb" in self.model_fields_set:
            _dict['receiverRoutingNumberISPB'] = None

        # set to None if receiver_document_number_type (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_document_number_type is None and "receiver_document_number_type" in self.model_fields_set:
            _dict['receiverDocumentNumberType'] = None

        # set to None if receiver_document_number_value (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_document_number_value is None and "receiver_document_number_value" in self.model_fields_set:
            _dict['receiverDocumentNumberValue'] = None

        # set to None if payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.payment_method is None and "payment_method" in self.model_fields_set:
            _dict['paymentMethod'] = None

        # set to None if reference_number (nullable) is None
        # and model_fields_set contains the field
        if self.reference_number is None and "reference_number" in self.model_fields_set:
            _dict['referenceNumber'] = None

        # set to None if receiver_reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.receiver_reference_id is None and "receiver_reference_id" in self.model_fields_set:
            _dict['receiverReferenceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payerName": obj.get("payerName"),
            "payerBranchNumber": obj.get("payerBranchNumber"),
            "payerAccountNumber": obj.get("payerAccountNumber"),
            "payerRoutingNumber": obj.get("payerRoutingNumber"),
            "payerRoutingNumberISPB": obj.get("payerRoutingNumberISPB"),
            "payerDocumentNumberType": obj.get("payerDocumentNumberType"),
            "payerDocumentNumberValue": obj.get("payerDocumentNumberValue"),
            "reason": obj.get("reason"),
            "receiverName": obj.get("receiverName"),
            "receiverBranchNumber": obj.get("receiverBranchNumber"),
            "receiverAccountNumber": obj.get("receiverAccountNumber"),
            "receiverRoutingNumber": obj.get("receiverRoutingNumber"),
            "receiverRoutingNumberISPB": obj.get("receiverRoutingNumberISPB"),
            "receiverDocumentNumberType": obj.get("receiverDocumentNumberType"),
            "receiverDocumentNumberValue": obj.get("receiverDocumentNumberValue"),
            "paymentMethod": obj.get("paymentMethod"),
            "referenceNumber": obj.get("referenceNumber"),
            "receiverReferenceId": obj.get("receiverReferenceId")
        })
        return _obj


