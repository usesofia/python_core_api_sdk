# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity

class TestCashFlowByCategoryReportEntity(unittest.TestCase):
    """CashFlowByCategoryReportEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashFlowByCategoryReportEntity:
        """Test CashFlowByCategoryReportEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CashFlowByCategoryReportEntity`
        """
        model = CashFlowByCategoryReportEntity()
        if include_optional:
            return CashFlowByCategoryReportEntity(
                items = [
                    openapi_client.models.cash_flow_by_category_report_item_entity.CashFlowByCategoryReportItemEntity(
                        category_id = '', 
                        category_name = '', 
                        absolute_value = 1.337, 
                        percentage = 1.337, )
                    ]
            )
        else:
            return CashFlowByCategoryReportEntity(
                items = [
                    openapi_client.models.cash_flow_by_category_report_item_entity.CashFlowByCategoryReportItemEntity(
                        category_id = '', 
                        category_name = '', 
                        absolute_value = 1.337, 
                        percentage = 1.337, )
                    ],
        )
        """

    def testCashFlowByCategoryReportEntity(self):
        """Test CashFlowByCategoryReportEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
