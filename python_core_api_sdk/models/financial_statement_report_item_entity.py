# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.financial_statement_outcome_report_data_entity import FinancialStatementOutcomeReportDataEntity
from python_core_api_sdk.models.financial_statement_outlfows_category_data import FinancialStatementOutlfowsCategoryData
from python_core_api_sdk.models.financial_statemente_entries_category_data import FinancialStatementeEntriesCategoryData
from typing import Optional, Set
from typing_extensions import Self

class FinancialStatementReportItemEntity(BaseModel):
    """
    FinancialStatementReportItemEntity
    """ # noqa: E501
    type: StrictStr
    entries_category_data: Optional[FinancialStatementeEntriesCategoryData] = Field(default=None, alias="entriesCategoryData")
    outflows_category_data: Optional[FinancialStatementOutlfowsCategoryData] = Field(default=None, alias="outflowsCategoryData")
    outcome_data: Optional[FinancialStatementOutcomeReportDataEntity] = Field(default=None, alias="outcomeData")
    __properties: ClassVar[List[str]] = ["type", "entriesCategoryData", "outflowsCategoryData", "outcomeData"]

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
        """Create an instance of FinancialStatementReportItemEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entries_category_data
        if self.entries_category_data:
            _dict['entriesCategoryData'] = self.entries_category_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outflows_category_data
        if self.outflows_category_data:
            _dict['outflowsCategoryData'] = self.outflows_category_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outcome_data
        if self.outcome_data:
            _dict['outcomeData'] = self.outcome_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FinancialStatementReportItemEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "entriesCategoryData": FinancialStatementeEntriesCategoryData.from_dict(obj["entriesCategoryData"]) if obj.get("entriesCategoryData") is not None else None,
            "outflowsCategoryData": FinancialStatementOutlfowsCategoryData.from_dict(obj["outflowsCategoryData"]) if obj.get("outflowsCategoryData") is not None else None,
            "outcomeData": FinancialStatementOutcomeReportDataEntity.from_dict(obj["outcomeData"]) if obj.get("outcomeData") is not None else None
        })
        return _obj


