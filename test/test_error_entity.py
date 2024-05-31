# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.error_entity import ErrorEntity

class TestErrorEntity(unittest.TestCase):
    """ErrorEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorEntity:
        """Test ErrorEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorEntity`
        """
        model = ErrorEntity()
        if include_optional:
            return ErrorEntity(
                field_id = '',
                messages = [
                    ''
                    ]
            )
        else:
            return ErrorEntity(
                field_id = '',
                messages = [
                    ''
                    ],
        )
        """

    def testErrorEntity(self):
        """Test ErrorEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
