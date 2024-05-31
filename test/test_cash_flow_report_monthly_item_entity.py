# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cash_flow_report_monthly_item_entity import CashFlowReportMonthlyItemEntity

class TestCashFlowReportMonthlyItemEntity(unittest.TestCase):
    """CashFlowReportMonthlyItemEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashFlowReportMonthlyItemEntity:
        """Test CashFlowReportMonthlyItemEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CashFlowReportMonthlyItemEntity`
        """
        model = CashFlowReportMonthlyItemEntity()
        if include_optional:
            return CashFlowReportMonthlyItemEntity(
                index = 1.337,
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                month = 1.337,
                label = '',
                min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                value = 1.337
            )
        else:
            return CashFlowReportMonthlyItemEntity(
                index = 1.337,
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                month = 1.337,
                label = '',
                min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCashFlowReportMonthlyItemEntity(self):
        """Test CashFlowReportMonthlyItemEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
