# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_users_controller_get(self) -> None:
        """Test case for users_controller_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
