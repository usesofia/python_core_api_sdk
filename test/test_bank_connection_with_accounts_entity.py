# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity

class TestBankConnectionWithAccountsEntity(unittest.TestCase):
    """BankConnectionWithAccountsEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankConnectionWithAccountsEntity:
        """Test BankConnectionWithAccountsEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankConnectionWithAccountsEntity`
        """
        model = BankConnectionWithAccountsEntity()
        if include_optional:
            return BankConnectionWithAccountsEntity(
                id = '',
                created_by_user_id = '',
                workspace_id = '',
                accounts = [
                    openapi_client.models.plain_bank_account_entity.PlainBankAccountEntity(
                        id = '', 
                        bank_connection_id = '', 
                        provider = '', 
                        provider_account_id = '', 
                        type = '', 
                        enabled = True, 
                        number = '', 
                        balance = 1.337, 
                        currency_code = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                enabled = True,
                provider = '',
                provider_item_id = '',
                history_range = '',
                connector_id = '',
                connector = openapi_client.models.bank_connector_entity.BankConnectorEntity(
                    id = '', 
                    provider = '', 
                    name = '', 
                    institution_url = '', 
                    image_url = '', 
                    primary_color = '', 
                    type = '', 
                    country = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BankConnectionWithAccountsEntity(
                id = '',
                created_by_user_id = '',
                workspace_id = '',
                accounts = [
                    openapi_client.models.plain_bank_account_entity.PlainBankAccountEntity(
                        id = '', 
                        bank_connection_id = '', 
                        provider = '', 
                        provider_account_id = '', 
                        type = '', 
                        enabled = True, 
                        number = '', 
                        balance = 1.337, 
                        currency_code = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                enabled = True,
                provider = '',
                provider_item_id = '',
                history_range = '',
                connector_id = '',
                connector = openapi_client.models.bank_connector_entity.BankConnectorEntity(
                    id = '', 
                    provider = '', 
                    name = '', 
                    institution_url = '', 
                    image_url = '', 
                    primary_color = '', 
                    type = '', 
                    country = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBankConnectionWithAccountsEntity(self):
        """Test BankConnectionWithAccountsEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
