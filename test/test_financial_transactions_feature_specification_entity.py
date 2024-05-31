# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.financial_transactions_feature_specification_entity import FinancialTransactionsFeatureSpecificationEntity

class TestFinancialTransactionsFeatureSpecificationEntity(unittest.TestCase):
    """FinancialTransactionsFeatureSpecificationEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialTransactionsFeatureSpecificationEntity:
        """Test FinancialTransactionsFeatureSpecificationEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinancialTransactionsFeatureSpecificationEntity`
        """
        model = FinancialTransactionsFeatureSpecificationEntity()
        if include_optional:
            return FinancialTransactionsFeatureSpecificationEntity(
                id = '',
                unlimited = True,
                max_per_month = 1.337,
                subscription_product_id = ''
            )
        else:
            return FinancialTransactionsFeatureSpecificationEntity(
                id = '',
                unlimited = True,
                subscription_product_id = '',
        )
        """

    def testFinancialTransactionsFeatureSpecificationEntity(self):
        """Test FinancialTransactionsFeatureSpecificationEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
