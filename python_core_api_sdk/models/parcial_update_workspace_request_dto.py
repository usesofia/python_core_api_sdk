# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from python_core_api_sdk.models.base_model import Model
from python_core_api_sdk import util


class ParcialUpdateWorkspaceRequestDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """ParcialUpdateWorkspaceRequestDto - a model defined in OpenAPI

        :param name: The name of this ParcialUpdateWorkspaceRequestDto.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ParcialUpdateWorkspaceRequestDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ParcialUpdateWorkspaceRequestDto of this ParcialUpdateWorkspaceRequestDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ParcialUpdateWorkspaceRequestDto.


        :return: The name of this ParcialUpdateWorkspaceRequestDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParcialUpdateWorkspaceRequestDto.


        :param name: The name of this ParcialUpdateWorkspaceRequestDto.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
