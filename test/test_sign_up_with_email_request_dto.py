# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.sign_up_with_email_request_dto import SignUpWithEmailRequestDto

class TestSignUpWithEmailRequestDto(unittest.TestCase):
    """SignUpWithEmailRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignUpWithEmailRequestDto:
        """Test SignUpWithEmailRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignUpWithEmailRequestDto`
        """
        model = SignUpWithEmailRequestDto()
        if include_optional:
            return SignUpWithEmailRequestDto(
                email = '',
                phone = '',
                password = '012345',
                email_verification_code = '4',
                phone_verification_code = '4'
            )
        else:
            return SignUpWithEmailRequestDto(
                email = '',
                phone = '',
                password = '012345',
                email_verification_code = '4',
                phone_verification_code = '4',
        )
        """

    def testSignUpWithEmailRequestDto(self):
        """Test SignUpWithEmailRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
