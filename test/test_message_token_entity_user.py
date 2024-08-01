# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from python_core_api_sdk.models.message_token_entity_user import MessageTokenEntityUser

class TestMessageTokenEntityUser(unittest.TestCase):
    """MessageTokenEntityUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageTokenEntityUser:
        """Test MessageTokenEntityUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageTokenEntityUser`
        """
        model = MessageTokenEntityUser()
        if include_optional:
            return MessageTokenEntityUser(
                id = '',
                email = '',
                phone = '',
                password_hash = '',
                is_root = True,
                workspaces = [
                    python_core_api_sdk.models.user_entity_workspaces_inner.UserEntity_workspaces_inner(
                        id = '', 
                        pretty_id = 'p0', 
                        name = '0', 
                        type = 'PERSONAL', 
                        creator_user_id = '', 
                        selected_personal_category_tree_id = '', 
                        selected_business_category_tree_id = '', 
                        hybrid_settings = python_core_api_sdk.models.user_entity_workspaces_inner_hybrid_settings.UserEntity_workspaces_inner_hybridSettings(
                            id = '', 
                            business_segment = 'ATTORNEY', 
                            other_business_description = '', ), 
                        business_settings = python_core_api_sdk.models.user_entity_workspaces_inner_hybrid_settings.UserEntity_workspaces_inner_hybridSettings(
                            id = '', 
                            business_segment = 'ATTORNEY', 
                            other_business_description = '', ), 
                        personal_settings = python_core_api_sdk.models.user_entity_workspaces_inner_personal_settings.UserEntity_workspaces_inner_personalSettings(
                            id = '', ), 
                        created_at = null, )
                    ],
                created_at = None
            )
        else:
            return MessageTokenEntityUser(
                id = '',
                email = '',
                phone = '',
                is_root = True,
                created_at = None,
        )
        """

    def testMessageTokenEntityUser(self):
        """Test MessageTokenEntityUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
