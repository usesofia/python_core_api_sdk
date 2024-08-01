# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage

class TestSyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage(unittest.TestCase):
    """SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage:
        """Test SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage`
        """
        model = SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage()
        if include_optional:
            return SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage(
                page_number = 56,
                page_size = 56,
                total_pages = 56,
                total_results = 56,
                transactions = [
                    python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner(
                        id = '', 
                        description = '', 
                        posted_date = null, 
                        amount = 56, 
                        direction_nature = 'CREDIT', 
                        status = 'PENDING', 
                        category_id = '', 
                        category_name = '', 
                        payment_data = python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner_paymentData(
                            payer_name = '', 
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
                            receiver_reference_id = '', ), 
                        credit_card_metadata = python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner_creditCardMetadata(
                            installment_number = 1.337, 
                            total_installments = 1.337, 
                            total_amount = 1.337, 
                            payee_mcc = 1.337, 
                            card_number = '', 
                            bill_id = '', ), )
                    ]
            )
        else:
            return SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage(
                page_number = 56,
                page_size = 56,
                total_pages = 56,
                total_results = 56,
                transactions = [
                    python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner(
                        id = '', 
                        description = '', 
                        posted_date = null, 
                        amount = 56, 
                        direction_nature = 'CREDIT', 
                        status = 'PENDING', 
                        category_id = '', 
                        category_name = '', 
                        payment_data = python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner_paymentData(
                            payer_name = '', 
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
                            receiver_reference_id = '', ), 
                        credit_card_metadata = python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata.SyncBankAccountTransactionsPageEndRequestDto_bankProviderTransactionsPage_transactions_inner_creditCardMetadata(
                            installment_number = 1.337, 
                            total_installments = 1.337, 
                            total_amount = 1.337, 
                            payee_mcc = 1.337, 
                            card_number = '', 
                            bill_id = '', ), )
                    ],
        )
        """

    def testSyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage(self):
        """Test SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
