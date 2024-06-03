# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from python_core_api_sdk.models.base_model import Model
from python_core_api_sdk import util


class CreateOrUpdateBankAccountRequestDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bank_connection_id: str=None, provider: str=None, provider_account_id: str=None, type: str=None, number: str=None, balance: float=None, currency_code: str=None, name: str=None):
        """CreateOrUpdateBankAccountRequestDto - a model defined in OpenAPI

        :param bank_connection_id: The bank_connection_id of this CreateOrUpdateBankAccountRequestDto.
        :param provider: The provider of this CreateOrUpdateBankAccountRequestDto.
        :param provider_account_id: The provider_account_id of this CreateOrUpdateBankAccountRequestDto.
        :param type: The type of this CreateOrUpdateBankAccountRequestDto.
        :param number: The number of this CreateOrUpdateBankAccountRequestDto.
        :param balance: The balance of this CreateOrUpdateBankAccountRequestDto.
        :param currency_code: The currency_code of this CreateOrUpdateBankAccountRequestDto.
        :param name: The name of this CreateOrUpdateBankAccountRequestDto.
        """
        self.openapi_types = {
            'bank_connection_id': str,
            'provider': str,
            'provider_account_id': str,
            'type': str,
            'number': str,
            'balance': float,
            'currency_code': str,
            'name': str
        }

        self.attribute_map = {
            'bank_connection_id': 'bankConnectionId',
            'provider': 'provider',
            'provider_account_id': 'providerAccountId',
            'type': 'type',
            'number': 'number',
            'balance': 'balance',
            'currency_code': 'currencyCode',
            'name': 'name'
        }

        self._bank_connection_id = bank_connection_id
        self._provider = provider
        self._provider_account_id = provider_account_id
        self._type = type
        self._number = number
        self._balance = balance
        self._currency_code = currency_code
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateOrUpdateBankAccountRequestDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CreateOrUpdateBankAccountRequestDto of this CreateOrUpdateBankAccountRequestDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bank_connection_id(self):
        """Gets the bank_connection_id of this CreateOrUpdateBankAccountRequestDto.


        :return: The bank_connection_id of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._bank_connection_id

    @bank_connection_id.setter
    def bank_connection_id(self, bank_connection_id):
        """Sets the bank_connection_id of this CreateOrUpdateBankAccountRequestDto.


        :param bank_connection_id: The bank_connection_id of this CreateOrUpdateBankAccountRequestDto.
        :type bank_connection_id: str
        """
        if bank_connection_id is None:
            raise ValueError("Invalid value for `bank_connection_id`, must not be `None`")

        self._bank_connection_id = bank_connection_id

    @property
    def provider(self):
        """Gets the provider of this CreateOrUpdateBankAccountRequestDto.


        :return: The provider of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateOrUpdateBankAccountRequestDto.


        :param provider: The provider of this CreateOrUpdateBankAccountRequestDto.
        :type provider: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider

    @property
    def provider_account_id(self):
        """Gets the provider_account_id of this CreateOrUpdateBankAccountRequestDto.


        :return: The provider_account_id of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._provider_account_id

    @provider_account_id.setter
    def provider_account_id(self, provider_account_id):
        """Sets the provider_account_id of this CreateOrUpdateBankAccountRequestDto.


        :param provider_account_id: The provider_account_id of this CreateOrUpdateBankAccountRequestDto.
        :type provider_account_id: str
        """
        if provider_account_id is None:
            raise ValueError("Invalid value for `provider_account_id`, must not be `None`")

        self._provider_account_id = provider_account_id

    @property
    def type(self):
        """Gets the type of this CreateOrUpdateBankAccountRequestDto.


        :return: The type of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateOrUpdateBankAccountRequestDto.


        :param type: The type of this CreateOrUpdateBankAccountRequestDto.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def number(self):
        """Gets the number of this CreateOrUpdateBankAccountRequestDto.


        :return: The number of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreateOrUpdateBankAccountRequestDto.


        :param number: The number of this CreateOrUpdateBankAccountRequestDto.
        :type number: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")

        self._number = number

    @property
    def balance(self):
        """Gets the balance of this CreateOrUpdateBankAccountRequestDto.


        :return: The balance of this CreateOrUpdateBankAccountRequestDto.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CreateOrUpdateBankAccountRequestDto.


        :param balance: The balance of this CreateOrUpdateBankAccountRequestDto.
        :type balance: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")

        self._balance = balance

    @property
    def currency_code(self):
        """Gets the currency_code of this CreateOrUpdateBankAccountRequestDto.


        :return: The currency_code of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CreateOrUpdateBankAccountRequestDto.


        :param currency_code: The currency_code of this CreateOrUpdateBankAccountRequestDto.
        :type currency_code: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def name(self):
        """Gets the name of this CreateOrUpdateBankAccountRequestDto.


        :return: The name of this CreateOrUpdateBankAccountRequestDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrUpdateBankAccountRequestDto.


        :param name: The name of this CreateOrUpdateBankAccountRequestDto.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
