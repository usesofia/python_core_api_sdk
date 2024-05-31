# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.subscription_product_entity import SubscriptionProductEntity

class TestSubscriptionProductEntity(unittest.TestCase):
    """SubscriptionProductEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionProductEntity:
        """Test SubscriptionProductEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionProductEntity`
        """
        model = SubscriptionProductEntity()
        if include_optional:
            return SubscriptionProductEntity(
                id = '',
                payment_system = '',
                payment_system_product_id = '',
                workspace_type = '',
                trial_period_in_days = 1.337,
                trial_already_used = True,
                connection_feature_specification = openapi_client.models.connection_feature_specification_entity.ConnectionFeatureSpecificationEntity(
                    id = '', 
                    unlimited = True, 
                    max = 1.337, 
                    subscription_product_id = '', ),
                financial_transactions_feature_specification = openapi_client.models.financial_transactions_feature_specification_entity.FinancialTransactionsFeatureSpecificationEntity(
                    id = '', 
                    unlimited = True, 
                    max_per_month = 1.337, 
                    subscription_product_id = '', ),
                ai_chat_feature_specification = openapi_client.models.ai_chat_feature_specification_entity.AiChatFeatureSpecificationEntity(
                    id = '', 
                    enabled = True, 
                    subscription_product_id = '', ),
                payments_manager_data = openapi_client.models.payments_manager_product_data_entity.PaymentsManagerProductDataEntity(
                    id = '', 
                    name = '', 
                    description = '', 
                    prices = [
                        openapi_client.models.payments_manager_product_price_entity.PaymentsManagerProductPriceEntity(
                            id = '', 
                            active = True, 
                            unit_amount = 1.337, 
                            interval = '', )
                        ], )
            )
        else:
            return SubscriptionProductEntity(
                id = '',
                payment_system = '',
                payment_system_product_id = '',
                workspace_type = '',
                connection_feature_specification = openapi_client.models.connection_feature_specification_entity.ConnectionFeatureSpecificationEntity(
                    id = '', 
                    unlimited = True, 
                    max = 1.337, 
                    subscription_product_id = '', ),
                financial_transactions_feature_specification = openapi_client.models.financial_transactions_feature_specification_entity.FinancialTransactionsFeatureSpecificationEntity(
                    id = '', 
                    unlimited = True, 
                    max_per_month = 1.337, 
                    subscription_product_id = '', ),
                ai_chat_feature_specification = openapi_client.models.ai_chat_feature_specification_entity.AiChatFeatureSpecificationEntity(
                    id = '', 
                    enabled = True, 
                    subscription_product_id = '', ),
                payments_manager_data = openapi_client.models.payments_manager_product_data_entity.PaymentsManagerProductDataEntity(
                    id = '', 
                    name = '', 
                    description = '', 
                    prices = [
                        openapi_client.models.payments_manager_product_price_entity.PaymentsManagerProductPriceEntity(
                            id = '', 
                            active = True, 
                            unit_amount = 1.337, 
                            interval = '', )
                        ], ),
        )
        """

    def testSubscriptionProductEntity(self):
        """Test SubscriptionProductEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
