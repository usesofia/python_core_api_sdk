# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from python_core_api_sdk.models.cash_flow_report_daily_item_entity import CashFlowReportDailyItemEntity
from python_core_api_sdk.models.cash_flow_report_monthly_item_entity import CashFlowReportMonthlyItemEntity
from python_core_api_sdk.models.cash_flow_report_weekly_item_entity import CashFlowReportWeeklyItemEntity
from typing import Optional, Set
from typing_extensions import Self

class CashFlowReportEntity(BaseModel):
    """
    CashFlowReportEntity
    """ # noqa: E501
    daily_balance_items: List[CashFlowReportDailyItemEntity] = Field(alias="dailyBalanceItems")
    daily_posted_income_items: List[CashFlowReportDailyItemEntity] = Field(alias="dailyPostedIncomeItems")
    daily_competency_income_items: List[CashFlowReportDailyItemEntity] = Field(alias="dailyCompetencyIncomeItems")
    daily_posted_outcome_items: List[CashFlowReportDailyItemEntity] = Field(alias="dailyPostedOutcomeItems")
    daily_competency_outcome_items: List[CashFlowReportDailyItemEntity] = Field(alias="dailyCompetencyOutcomeItems")
    weekly_balance_items: List[CashFlowReportWeeklyItemEntity] = Field(alias="weeklyBalanceItems")
    weekly_posted_income_items: List[CashFlowReportWeeklyItemEntity] = Field(alias="weeklyPostedIncomeItems")
    weekly_competency_income_items: List[CashFlowReportWeeklyItemEntity] = Field(alias="weeklyCompetencyIncomeItems")
    weekly_posted_outcome_items: List[CashFlowReportWeeklyItemEntity] = Field(alias="weeklyPostedOutcomeItems")
    weekly_competency_outcome_items: List[CashFlowReportWeeklyItemEntity] = Field(alias="weeklyCompetencyOutcomeItems")
    monthly_balance_items: List[CashFlowReportMonthlyItemEntity] = Field(alias="monthlyBalanceItems")
    monthly_posted_income_items: List[CashFlowReportMonthlyItemEntity] = Field(alias="monthlyPostedIncomeItems")
    monthly_competency_income_items: List[CashFlowReportMonthlyItemEntity] = Field(alias="monthlyCompetencyIncomeItems")
    monthly_posted_outcome_items: List[CashFlowReportMonthlyItemEntity] = Field(alias="monthlyPostedOutcomeItems")
    monthly_competency_outcome_items: List[CashFlowReportMonthlyItemEntity] = Field(alias="monthlyCompetencyOutcomeItems")
    __properties: ClassVar[List[str]] = ["dailyBalanceItems", "dailyPostedIncomeItems", "dailyCompetencyIncomeItems", "dailyPostedOutcomeItems", "dailyCompetencyOutcomeItems", "weeklyBalanceItems", "weeklyPostedIncomeItems", "weeklyCompetencyIncomeItems", "weeklyPostedOutcomeItems", "weeklyCompetencyOutcomeItems", "monthlyBalanceItems", "monthlyPostedIncomeItems", "monthlyCompetencyIncomeItems", "monthlyPostedOutcomeItems", "monthlyCompetencyOutcomeItems"]

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
        """Create an instance of CashFlowReportEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in daily_balance_items (list)
        _items = []
        if self.daily_balance_items:
            for _item in self.daily_balance_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyBalanceItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_posted_income_items (list)
        _items = []
        if self.daily_posted_income_items:
            for _item in self.daily_posted_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyPostedIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_competency_income_items (list)
        _items = []
        if self.daily_competency_income_items:
            for _item in self.daily_competency_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyCompetencyIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_posted_outcome_items (list)
        _items = []
        if self.daily_posted_outcome_items:
            for _item in self.daily_posted_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyPostedOutcomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in daily_competency_outcome_items (list)
        _items = []
        if self.daily_competency_outcome_items:
            for _item in self.daily_competency_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dailyCompetencyOutcomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_balance_items (list)
        _items = []
        if self.weekly_balance_items:
            for _item in self.weekly_balance_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyBalanceItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_posted_income_items (list)
        _items = []
        if self.weekly_posted_income_items:
            for _item in self.weekly_posted_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyPostedIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_competency_income_items (list)
        _items = []
        if self.weekly_competency_income_items:
            for _item in self.weekly_competency_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyCompetencyIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_posted_outcome_items (list)
        _items = []
        if self.weekly_posted_outcome_items:
            for _item in self.weekly_posted_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyPostedOutcomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in weekly_competency_outcome_items (list)
        _items = []
        if self.weekly_competency_outcome_items:
            for _item in self.weekly_competency_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['weeklyCompetencyOutcomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_balance_items (list)
        _items = []
        if self.monthly_balance_items:
            for _item in self.monthly_balance_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthlyBalanceItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_posted_income_items (list)
        _items = []
        if self.monthly_posted_income_items:
            for _item in self.monthly_posted_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthlyPostedIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_competency_income_items (list)
        _items = []
        if self.monthly_competency_income_items:
            for _item in self.monthly_competency_income_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthlyCompetencyIncomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_posted_outcome_items (list)
        _items = []
        if self.monthly_posted_outcome_items:
            for _item in self.monthly_posted_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthlyPostedOutcomeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_competency_outcome_items (list)
        _items = []
        if self.monthly_competency_outcome_items:
            for _item in self.monthly_competency_outcome_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthlyCompetencyOutcomeItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CashFlowReportEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dailyBalanceItems": [CashFlowReportDailyItemEntity.from_dict(_item) for _item in obj["dailyBalanceItems"]] if obj.get("dailyBalanceItems") is not None else None,
            "dailyPostedIncomeItems": [CashFlowReportDailyItemEntity.from_dict(_item) for _item in obj["dailyPostedIncomeItems"]] if obj.get("dailyPostedIncomeItems") is not None else None,
            "dailyCompetencyIncomeItems": [CashFlowReportDailyItemEntity.from_dict(_item) for _item in obj["dailyCompetencyIncomeItems"]] if obj.get("dailyCompetencyIncomeItems") is not None else None,
            "dailyPostedOutcomeItems": [CashFlowReportDailyItemEntity.from_dict(_item) for _item in obj["dailyPostedOutcomeItems"]] if obj.get("dailyPostedOutcomeItems") is not None else None,
            "dailyCompetencyOutcomeItems": [CashFlowReportDailyItemEntity.from_dict(_item) for _item in obj["dailyCompetencyOutcomeItems"]] if obj.get("dailyCompetencyOutcomeItems") is not None else None,
            "weeklyBalanceItems": [CashFlowReportWeeklyItemEntity.from_dict(_item) for _item in obj["weeklyBalanceItems"]] if obj.get("weeklyBalanceItems") is not None else None,
            "weeklyPostedIncomeItems": [CashFlowReportWeeklyItemEntity.from_dict(_item) for _item in obj["weeklyPostedIncomeItems"]] if obj.get("weeklyPostedIncomeItems") is not None else None,
            "weeklyCompetencyIncomeItems": [CashFlowReportWeeklyItemEntity.from_dict(_item) for _item in obj["weeklyCompetencyIncomeItems"]] if obj.get("weeklyCompetencyIncomeItems") is not None else None,
            "weeklyPostedOutcomeItems": [CashFlowReportWeeklyItemEntity.from_dict(_item) for _item in obj["weeklyPostedOutcomeItems"]] if obj.get("weeklyPostedOutcomeItems") is not None else None,
            "weeklyCompetencyOutcomeItems": [CashFlowReportWeeklyItemEntity.from_dict(_item) for _item in obj["weeklyCompetencyOutcomeItems"]] if obj.get("weeklyCompetencyOutcomeItems") is not None else None,
            "monthlyBalanceItems": [CashFlowReportMonthlyItemEntity.from_dict(_item) for _item in obj["monthlyBalanceItems"]] if obj.get("monthlyBalanceItems") is not None else None,
            "monthlyPostedIncomeItems": [CashFlowReportMonthlyItemEntity.from_dict(_item) for _item in obj["monthlyPostedIncomeItems"]] if obj.get("monthlyPostedIncomeItems") is not None else None,
            "monthlyCompetencyIncomeItems": [CashFlowReportMonthlyItemEntity.from_dict(_item) for _item in obj["monthlyCompetencyIncomeItems"]] if obj.get("monthlyCompetencyIncomeItems") is not None else None,
            "monthlyPostedOutcomeItems": [CashFlowReportMonthlyItemEntity.from_dict(_item) for _item in obj["monthlyPostedOutcomeItems"]] if obj.get("monthlyPostedOutcomeItems") is not None else None,
            "monthlyCompetencyOutcomeItems": [CashFlowReportMonthlyItemEntity.from_dict(_item) for _item in obj["monthlyCompetencyOutcomeItems"]] if obj.get("monthlyCompetencyOutcomeItems") is not None else None
        })
        return _obj


