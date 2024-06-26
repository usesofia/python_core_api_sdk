# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.bank_transaction_entity import BankTransactionEntity

class TestBankTransactionEntity(unittest.TestCase):
    """BankTransactionEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankTransactionEntity:
        """Test BankTransactionEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankTransactionEntity`
        """
        model = BankTransactionEntity()
        if include_optional:
            return BankTransactionEntity(
                id = '',
                account_id = '',
                account = openapi_client.models.bank_account_entity.BankAccountEntity(
                    id = '', 
                    bank_connection_id = '', 
                    bank_connection = openapi_client.models.bank_connection_entity.BankConnectionEntity(
                        id = '', 
                        created_by_user_id = '', 
                        workspace_id = '', 
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
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    provider = '', 
                    provider_account_id = '', 
                    type = '', 
                    enabled = True, 
                    number = '', 
                    balance = 1.337, 
                    currency_code = '', 
                    name = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                workspace_id = '',
                provider = 'PLUGGY',
                provider_transaction_id = '',
                original_description = '',
                description = '',
                posted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                competency_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                amount = 1.337,
                type = 'DEBIT',
                status = 'PENDING',
                legal_nature = 'PERSONAL',
                provider_category_id = '',
                provider_category_name = '',
                category_id = '',
                category = openapi_client.models.bank_transaction_category_plain_entity.BankTransactionCategoryPlainEntity(
                    id = '', 
                    name = '', 
                    nature = '', 
                    parent_id = '', ),
                tags = [
                    openapi_client.models.bank_transaction_tag_entity.BankTransactionTagEntity(
                        id = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                payment_data_id = '',
                payment_data = openapi_client.models.bank_transaction_payment_data_entity.BankTransactionPaymentDataEntity(
                    id = '', 
                    transaction_id = '', 
                    payeer_name = '', 
                    payer_branch_number = '', 
                    payer_account_number = '', 
                    payer_routing_number = '', 
                    payer_routing_number_ispb = '', 
                    payer_document_number_type = '', 
                    payer_document_number_value = '', 
                    reason = '', 
                    receiver_name = '', 
                    receiver_branch_number = '', 
                    receiver_account_number = '', 
                    receiver_routing_number = '', 
                    receiver_routing_number_ispb = '', 
                    receiver_document_number_type = '', 
                    receiver_document_number_value = '', 
                    payment_method = '', 
                    reference_number = '', 
                    receiver_reference_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                credit_card_metadata_id = '',
                credit_card_metadata = openapi_client.models.bank_transaction_credit_card_metadata_entity.BankTransactionCreditCardMetadataEntity(
                    id = '', 
                    transaction_id = '', 
                    installment_number = 1.337, 
                    total_installments = 1.337, 
                    total_amount = 1.337, 
                    payee_mcc = 1.337, 
                    card_number = '', 
                    bill_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                best_guess_category_id = '',
                best_guess_category = openapi_client.models.bank_transaction_category_plain_entity.BankTransactionCategoryPlainEntity(
                    id = '', 
                    name = '', 
                    nature = '', 
                    parent_id = '', ),
                ignored_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                confirmed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BankTransactionEntity(
                id = '',
                account_id = '',
                account = openapi_client.models.bank_account_entity.BankAccountEntity(
                    id = '', 
                    bank_connection_id = '', 
                    bank_connection = openapi_client.models.bank_connection_entity.BankConnectionEntity(
                        id = '', 
                        created_by_user_id = '', 
                        workspace_id = '', 
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
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    provider = '', 
                    provider_account_id = '', 
                    type = '', 
                    enabled = True, 
                    number = '', 
                    balance = 1.337, 
                    currency_code = '', 
                    name = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                workspace_id = '',
                provider = 'PLUGGY',
                provider_transaction_id = '',
                original_description = '',
                description = '',
                posted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                competency_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                amount = 1.337,
                type = 'DEBIT',
                status = 'PENDING',
                legal_nature = 'PERSONAL',
                tags = [
                    openapi_client.models.bank_transaction_tag_entity.BankTransactionTagEntity(
                        id = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBankTransactionEntity(self):
        """Test BankTransactionEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
