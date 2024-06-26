# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.payments_manager_product_data_entity import PaymentsManagerProductDataEntity

class TestPaymentsManagerProductDataEntity(unittest.TestCase):
    """PaymentsManagerProductDataEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentsManagerProductDataEntity:
        """Test PaymentsManagerProductDataEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentsManagerProductDataEntity`
        """
        model = PaymentsManagerProductDataEntity()
        if include_optional:
            return PaymentsManagerProductDataEntity(
                id = '',
                name = '',
                description = '',
                prices = [
                    openapi_client.models.payments_manager_product_price_entity.PaymentsManagerProductPriceEntity(
                        id = '', 
                        active = True, 
                        unit_amount = 1.337, 
                        interval = '', )
                    ]
            )
        else:
            return PaymentsManagerProductDataEntity(
                id = '',
                name = '',
                description = '',
                prices = [
                    openapi_client.models.payments_manager_product_price_entity.PaymentsManagerProductPriceEntity(
                        id = '', 
                        active = True, 
                        unit_amount = 1.337, 
                        interval = '', )
                    ],
        )
        """

    def testPaymentsManagerProductDataEntity(self):
        """Test PaymentsManagerProductDataEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
