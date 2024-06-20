# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.verify_phone_verification_code_request_dto import VerifyPhoneVerificationCodeRequestDto

class TestVerifyPhoneVerificationCodeRequestDto(unittest.TestCase):
    """VerifyPhoneVerificationCodeRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifyPhoneVerificationCodeRequestDto:
        """Test VerifyPhoneVerificationCodeRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifyPhoneVerificationCodeRequestDto`
        """
        model = VerifyPhoneVerificationCodeRequestDto()
        if include_optional:
            return VerifyPhoneVerificationCodeRequestDto(
                phone = '',
                purpose = 'SIGN_UP',
                code = '4'
            )
        else:
            return VerifyPhoneVerificationCodeRequestDto(
                phone = '',
                purpose = 'SIGN_UP',
                code = '4',
        )
        """

    def testVerifyPhoneVerificationCodeRequestDto(self):
        """Test VerifyPhoneVerificationCodeRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
