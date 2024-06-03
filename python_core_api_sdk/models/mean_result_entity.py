# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from python_core_api_sdk.models.base_model import Model
from python_core_api_sdk.models.mean_result_subcategory_item_entity import MeanResultSubcategoryItemEntity
from python_core_api_sdk import util


class MeanResultEntity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, amount_in_cents: float=None, subcategories: List[MeanResultSubcategoryItemEntity]=None):
        """MeanResultEntity - a model defined in OpenAPI

        :param amount_in_cents: The amount_in_cents of this MeanResultEntity.
        :param subcategories: The subcategories of this MeanResultEntity.
        """
        self.openapi_types = {
            'amount_in_cents': float,
            'subcategories': List[MeanResultSubcategoryItemEntity]
        }

        self.attribute_map = {
            'amount_in_cents': 'amountInCents',
            'subcategories': 'subcategories'
        }

        self._amount_in_cents = amount_in_cents
        self._subcategories = subcategories

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MeanResultEntity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MeanResultEntity of this MeanResultEntity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount_in_cents(self):
        """Gets the amount_in_cents of this MeanResultEntity.


        :return: The amount_in_cents of this MeanResultEntity.
        :rtype: float
        """
        return self._amount_in_cents

    @amount_in_cents.setter
    def amount_in_cents(self, amount_in_cents):
        """Sets the amount_in_cents of this MeanResultEntity.


        :param amount_in_cents: The amount_in_cents of this MeanResultEntity.
        :type amount_in_cents: float
        """
        if amount_in_cents is None:
            raise ValueError("Invalid value for `amount_in_cents`, must not be `None`")

        self._amount_in_cents = amount_in_cents

    @property
    def subcategories(self):
        """Gets the subcategories of this MeanResultEntity.


        :return: The subcategories of this MeanResultEntity.
        :rtype: List[MeanResultSubcategoryItemEntity]
        """
        return self._subcategories

    @subcategories.setter
    def subcategories(self, subcategories):
        """Sets the subcategories of this MeanResultEntity.


        :param subcategories: The subcategories of this MeanResultEntity.
        :type subcategories: List[MeanResultSubcategoryItemEntity]
        """

        self._subcategories = subcategories
