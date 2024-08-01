# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.bank_connection_entity_accounts_inner import BankConnectionEntityAccountsInner

class TestBankConnectionEntityAccountsInner(unittest.TestCase):
    """BankConnectionEntityAccountsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankConnectionEntityAccountsInner:
        """Test BankConnectionEntityAccountsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankConnectionEntityAccountsInner`
        """
        model = BankConnectionEntityAccountsInner()
        if include_optional:
            return BankConnectionEntityAccountsInner(
                id = '',
                bank_connection_id = '',
                provider = 'PLUGGY',
                provider_account_id = '',
                type = 'CHECKING',
                enabled = True,
                number = '',
                balance = 56,
                currency_code = '',
                name = '',
                created_at = None,
                updated_at = None
            )
        else:
            return BankConnectionEntityAccountsInner(
                id = '',
                bank_connection_id = '',
                provider = 'PLUGGY',
                provider_account_id = '',
                type = 'CHECKING',
                enabled = True,
                number = '',
                balance = 56,
                currency_code = '',
                name = '',
                created_at = None,
                updated_at = None,
        )
        """

    def testBankConnectionEntityAccountsInner(self):
        """Test BankConnectionEntityAccountsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
