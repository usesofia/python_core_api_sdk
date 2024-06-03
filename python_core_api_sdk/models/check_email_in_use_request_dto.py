# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from python_core_api_sdk.models.base_model import Model
from python_core_api_sdk import util


class CheckEmailInUseRequestDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email: str=None):
        """CheckEmailInUseRequestDto - a model defined in OpenAPI

        :param email: The email of this CheckEmailInUseRequestDto.
        """
        self.openapi_types = {
            'email': str
        }

        self.attribute_map = {
            'email': 'email'
        }

        self._email = email

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CheckEmailInUseRequestDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CheckEmailInUseRequestDto of this CheckEmailInUseRequestDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this CheckEmailInUseRequestDto.


        :return: The email of this CheckEmailInUseRequestDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CheckEmailInUseRequestDto.


        :param email: The email of this CheckEmailInUseRequestDto.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email
