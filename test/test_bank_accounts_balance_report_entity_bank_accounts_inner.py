# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.bank_accounts_balance_report_entity_bank_accounts_inner import BankAccountsBalanceReportEntityBankAccountsInner

class TestBankAccountsBalanceReportEntityBankAccountsInner(unittest.TestCase):
    """BankAccountsBalanceReportEntityBankAccountsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankAccountsBalanceReportEntityBankAccountsInner:
        """Test BankAccountsBalanceReportEntityBankAccountsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankAccountsBalanceReportEntityBankAccountsInner`
        """
        model = BankAccountsBalanceReportEntityBankAccountsInner()
        if include_optional:
            return BankAccountsBalanceReportEntityBankAccountsInner(
                id = '',
                bank_connection_id = '',
                bank_connection = python_core_api_sdk.models.bank_account_entity_bank_connection.BankAccountEntity_bankConnection(
                    id = '', 
                    created_by_user_id = '', 
                    workspace_id = '', 
                    enabled = True, 
                    provider = 'PLUGGY', 
                    provider_item_id = '', 
                    history_range = 'ONE_DAY', 
                    connector_id = '', 
                    connector = python_core_api_sdk.models.bank_connection_entity_connector.BankConnectionEntity_connector(
                        id = '', 
                        provider = 'PLUGGY', 
                        name = '', 
                        institution_url = '', 
                        image_url = '', 
                        primary_color = '', 
                        type = 'PERSONAL_BANK', 
                        country = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                provider = 'PLUGGY',
                provider_account_id = '',
                type = 'CHECKING',
                enabled = True,
                number = '',
                balance = 56,
                currency_code = '',
                name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BankAccountsBalanceReportEntityBankAccountsInner(
                id = '',
                bank_connection_id = '',
                bank_connection = python_core_api_sdk.models.bank_account_entity_bank_connection.BankAccountEntity_bankConnection(
                    id = '', 
                    created_by_user_id = '', 
                    workspace_id = '', 
                    enabled = True, 
                    provider = 'PLUGGY', 
                    provider_item_id = '', 
                    history_range = 'ONE_DAY', 
                    connector_id = '', 
                    connector = python_core_api_sdk.models.bank_connection_entity_connector.BankConnectionEntity_connector(
                        id = '', 
                        provider = 'PLUGGY', 
                        name = '', 
                        institution_url = '', 
                        image_url = '', 
                        primary_color = '', 
                        type = 'PERSONAL_BANK', 
                        country = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                provider = 'PLUGGY',
                provider_account_id = '',
                type = 'CHECKING',
                enabled = True,
                number = '',
                balance = 56,
                currency_code = '',
                name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBankAccountsBalanceReportEntityBankAccountsInner(self):
        """Test BankAccountsBalanceReportEntityBankAccountsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
