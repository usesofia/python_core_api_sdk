# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_profile_request_dto import CreateProfileRequestDto

class TestCreateProfileRequestDto(unittest.TestCase):
    """CreateProfileRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateProfileRequestDto:
        """Test CreateProfileRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProfileRequestDto`
        """
        model = CreateProfileRequestDto()
        if include_optional:
            return CreateProfileRequestDto(
                full_name = '',
                phone = '',
                birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CreateProfileRequestDto(
                full_name = '',
                phone = '',
                birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCreateProfileRequestDto(self):
        """Test CreateProfileRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
