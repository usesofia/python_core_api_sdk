# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.sync_bank_item_request_dto import SyncBankItemRequestDto

class TestSyncBankItemRequestDto(unittest.TestCase):
    """SyncBankItemRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SyncBankItemRequestDto:
        """Test SyncBankItemRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncBankItemRequestDto`
        """
        model = SyncBankItemRequestDto()
        if include_optional:
            return SyncBankItemRequestDto(
                provider_item_id = '',
                provider = 'PLUGGY'
            )
        else:
            return SyncBankItemRequestDto(
                provider_item_id = '',
                provider = 'PLUGGY',
        )
        """

    def testSyncBankItemRequestDto(self):
        """Test SyncBankItemRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
