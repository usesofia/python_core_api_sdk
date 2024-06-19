# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.send_phone_verification_code_request_dto import SendPhoneVerificationCodeRequestDto

class TestSendPhoneVerificationCodeRequestDto(unittest.TestCase):
    """SendPhoneVerificationCodeRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendPhoneVerificationCodeRequestDto:
        """Test SendPhoneVerificationCodeRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendPhoneVerificationCodeRequestDto`
        """
        model = SendPhoneVerificationCodeRequestDto()
        if include_optional:
            return SendPhoneVerificationCodeRequestDto(
                phone = ''
            )
        else:
            return SendPhoneVerificationCodeRequestDto(
                phone = '',
        )
        """

    def testSendPhoneVerificationCodeRequestDto(self):
        """Test SendPhoneVerificationCodeRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()