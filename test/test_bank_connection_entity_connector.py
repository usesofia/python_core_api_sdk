# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.bank_connection_entity_connector import BankConnectionEntityConnector

class TestBankConnectionEntityConnector(unittest.TestCase):
    """BankConnectionEntityConnector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankConnectionEntityConnector:
        """Test BankConnectionEntityConnector
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankConnectionEntityConnector`
        """
        model = BankConnectionEntityConnector()
        if include_optional:
            return BankConnectionEntityConnector(
                id = '',
                provider = 'PLUGGY',
                name = '',
                institution_url = '',
                image_url = '',
                primary_color = '',
                type = 'PERSONAL_BANK',
                country = '',
                created_at = None,
                updated_at = None
            )
        else:
            return BankConnectionEntityConnector(
                id = '',
                provider = 'PLUGGY',
                name = '',
                institution_url = '',
                image_url = '',
                primary_color = '',
                type = 'PERSONAL_BANK',
                country = '',
                created_at = None,
                updated_at = None,
        )
        """

    def testBankConnectionEntityConnector(self):
        """Test BankConnectionEntityConnector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()