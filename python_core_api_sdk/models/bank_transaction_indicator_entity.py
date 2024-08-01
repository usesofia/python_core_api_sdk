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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from python_core_api_sdk.models.balance_point_result_entity import BalancePointResultEntity
from python_core_api_sdk.models.dre_line_outcome_result_entity import DreLineOutcomeResultEntity
from python_core_api_sdk.models.mean_result_entity import MeanResultEntity
from python_core_api_sdk.models.proportion_result_entity import ProportionResultEntity
from typing import Optional, Set
from typing_extensions import Self

class BankTransactionIndicatorEntity(BaseModel):
    """
    BankTransactionIndicatorEntity
    """ # noqa: E501
    id: StrictStr
    pretty_id: StrictStr = Field(alias="prettyId")
    type: StrictStr
    name: StrictStr
    description: StrictStr
    data: Dict[str, Any]
    dre_line_outcome_result: Optional[DreLineOutcomeResultEntity] = Field(default=None, alias="dreLineOutcomeResult")
    balance_point_result: Optional[BalancePointResultEntity] = Field(default=None, alias="balancePointResult")
    mean_result: Optional[MeanResultEntity] = Field(default=None, alias="meanResult")
    proportion_result: Optional[ProportionResultEntity] = Field(default=None, alias="proportionResult")
    __properties: ClassVar[List[str]] = ["id", "prettyId", "type", "name", "description", "data", "dreLineOutcomeResult", "balancePointResult", "meanResult", "proportionResult"]

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
        """Create an instance of BankTransactionIndicatorEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dre_line_outcome_result
        if self.dre_line_outcome_result:
            _dict['dreLineOutcomeResult'] = self.dre_line_outcome_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of balance_point_result
        if self.balance_point_result:
            _dict['balancePointResult'] = self.balance_point_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mean_result
        if self.mean_result:
            _dict['meanResult'] = self.mean_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proportion_result
        if self.proportion_result:
            _dict['proportionResult'] = self.proportion_result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransactionIndicatorEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "prettyId": obj.get("prettyId"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "data": obj.get("data"),
            "dreLineOutcomeResult": DreLineOutcomeResultEntity.from_dict(obj["dreLineOutcomeResult"]) if obj.get("dreLineOutcomeResult") is not None else None,
            "balancePointResult": BalancePointResultEntity.from_dict(obj["balancePointResult"]) if obj.get("balancePointResult") is not None else None,
            "meanResult": MeanResultEntity.from_dict(obj["meanResult"]) if obj.get("meanResult") is not None else None,
            "proportionResult": ProportionResultEntity.from_dict(obj["proportionResult"]) if obj.get("proportionResult") is not None else None
        })
        return _obj


