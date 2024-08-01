# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.sync_bank_account_transactions_page_begin_request_dto import SyncBankAccountTransactionsPageBeginRequestDto

class TestSyncBankAccountTransactionsPageBeginRequestDto(unittest.TestCase):
    """SyncBankAccountTransactionsPageBeginRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncBankAccountTransactionsPageBeginRequestDto:
        """Test SyncBankAccountTransactionsPageBeginRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncBankAccountTransactionsPageBeginRequestDto`
        """
        model = SyncBankAccountTransactionsPageBeginRequestDto()
        if include_optional:
            return SyncBankAccountTransactionsPageBeginRequestDto(
                sync_item_id = '',
                page_number = 56
            )
        else:
            return SyncBankAccountTransactionsPageBeginRequestDto(
                sync_item_id = '',
                page_number = 56,
        )
        """

    def testSyncBankAccountTransactionsPageBeginRequestDto(self):
        """Test SyncBankAccountTransactionsPageBeginRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()