# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pluggy_connect_token_entity import PluggyConnectTokenEntity

class TestPluggyConnectTokenEntity(unittest.TestCase):
    """PluggyConnectTokenEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PluggyConnectTokenEntity:
        """Test PluggyConnectTokenEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PluggyConnectTokenEntity`
        """
        model = PluggyConnectTokenEntity()
        if include_optional:
            return PluggyConnectTokenEntity(
                access_token = ''
            )
        else:
            return PluggyConnectTokenEntity(
                access_token = '',
        )
        """

    def testPluggyConnectTokenEntity(self):
        """Test PluggyConnectTokenEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
