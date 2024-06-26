# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cash_flow_report_entity import CashFlowReportEntity

class TestCashFlowReportEntity(unittest.TestCase):
    """CashFlowReportEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CashFlowReportEntity:
        """Test CashFlowReportEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CashFlowReportEntity`
        """
        model = CashFlowReportEntity()
        if include_optional:
            return CashFlowReportEntity(
                daily_balance_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_posted_income_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_competency_income_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_balance_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_posted_income_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_competency_income_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_balance_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_posted_income_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_competency_income_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ]
            )
        else:
            return CashFlowReportEntity(
                daily_balance_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_posted_income_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_competency_income_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                daily_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_daily_item_entity.CashFlowReportDailyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        day_of_year = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_balance_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_posted_income_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_competency_income_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                weekly_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_weekly_item_entity.CashFlowReportWeeklyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        week = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_balance_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_posted_income_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_competency_income_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_posted_outcome_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
                monthly_competency_outcome_items = [
                    openapi_client.models.cash_flow_report_monthly_item_entity.CashFlowReportMonthlyItemEntity(
                        index = 1.337, 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        month = 1.337, 
                        label = '', 
                        min_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        max_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        value = 1.337, )
                    ],
        )
        """

    def testCashFlowReportEntity(self):
        """Test CashFlowReportEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
