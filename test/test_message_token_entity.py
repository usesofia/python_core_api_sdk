# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.message_token_entity import MessageTokenEntity

class TestMessageTokenEntity(unittest.TestCase):
    """MessageTokenEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageTokenEntity:
        """Test MessageTokenEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageTokenEntity`
        """
        model = MessageTokenEntity()
        if include_optional:
            return MessageTokenEntity(
                id = '',
                workspace_id = '',
                workspace = openapi_client.models.workspace_entity.WorkspaceEntity(
                    id = '', 
                    pretty_id = '', 
                    name = '', 
                    type = '', 
                    creator_user_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    selected_personal_category_tree_id = '', 
                    selected_business_category_tree_id = '', ),
                user_id = '',
                user = openapi_client.models.user_entity.UserEntity(
                    id = '', 
                    email = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    password_hash = '', ),
                provider = 'FIREBASE_MESSAGING',
                platform = 'WEB',
                device_id = '',
                token = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return MessageTokenEntity(
                id = '',
                workspace_id = '',
                workspace = openapi_client.models.workspace_entity.WorkspaceEntity(
                    id = '', 
                    pretty_id = '', 
                    name = '', 
                    type = '', 
                    creator_user_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    selected_personal_category_tree_id = '', 
                    selected_business_category_tree_id = '', ),
                user_id = '',
                user = openapi_client.models.user_entity.UserEntity(
                    id = '', 
                    email = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    password_hash = '', ),
                provider = 'FIREBASE_MESSAGING',
                platform = 'WEB',
                device_id = '',
                token = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testMessageTokenEntity(self):
        """Test MessageTokenEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
