# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.partial_update_profile_request_dto import PartialUpdateProfileRequestDto

class TestPartialUpdateProfileRequestDto(unittest.TestCase):
    """PartialUpdateProfileRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartialUpdateProfileRequestDto:
        """Test PartialUpdateProfileRequestDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartialUpdateProfileRequestDto`
        """
        model = PartialUpdateProfileRequestDto()
        if include_optional:
            return PartialUpdateProfileRequestDto(
                full_name = '',
                birth_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PartialUpdateProfileRequestDto(
        )
        """

    def testPartialUpdateProfileRequestDto(self):
        """Test PartialUpdateProfileRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
