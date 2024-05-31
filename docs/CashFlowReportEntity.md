# CashFlowReportEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily_balance_items** | [**List[CashFlowReportDailyItemEntity]**](CashFlowReportDailyItemEntity.md) |  | 
**daily_posted_income_items** | [**List[CashFlowReportDailyItemEntity]**](CashFlowReportDailyItemEntity.md) |  | 
**daily_competency_income_items** | [**List[CashFlowReportDailyItemEntity]**](CashFlowReportDailyItemEntity.md) |  | 
**daily_posted_outcome_items** | [**List[CashFlowReportDailyItemEntity]**](CashFlowReportDailyItemEntity.md) |  | 
**daily_competency_outcome_items** | [**List[CashFlowReportDailyItemEntity]**](CashFlowReportDailyItemEntity.md) |  | 
**weekly_balance_items** | [**List[CashFlowReportWeeklyItemEntity]**](CashFlowReportWeeklyItemEntity.md) |  | 
**weekly_posted_income_items** | [**List[CashFlowReportWeeklyItemEntity]**](CashFlowReportWeeklyItemEntity.md) |  | 
**weekly_competency_income_items** | [**List[CashFlowReportWeeklyItemEntity]**](CashFlowReportWeeklyItemEntity.md) |  | 
**weekly_posted_outcome_items** | [**List[CashFlowReportWeeklyItemEntity]**](CashFlowReportWeeklyItemEntity.md) |  | 
**weekly_competency_outcome_items** | [**List[CashFlowReportWeeklyItemEntity]**](CashFlowReportWeeklyItemEntity.md) |  | 
**monthly_balance_items** | [**List[CashFlowReportMonthlyItemEntity]**](CashFlowReportMonthlyItemEntity.md) |  | 
**monthly_posted_income_items** | [**List[CashFlowReportMonthlyItemEntity]**](CashFlowReportMonthlyItemEntity.md) |  | 
**monthly_competency_income_items** | [**List[CashFlowReportMonthlyItemEntity]**](CashFlowReportMonthlyItemEntity.md) |  | 
**monthly_posted_outcome_items** | [**List[CashFlowReportMonthlyItemEntity]**](CashFlowReportMonthlyItemEntity.md) |  | 
**monthly_competency_outcome_items** | [**List[CashFlowReportMonthlyItemEntity]**](CashFlowReportMonthlyItemEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowReportEntity from a JSON string
cash_flow_report_entity_instance = CashFlowReportEntity.from_json(json)
# print the JSON string representation of the object
print(CashFlowReportEntity.to_json())

# convert the object into a dict
cash_flow_report_entity_dict = cash_flow_report_entity_instance.to_dict()
# create an instance of CashFlowReportEntity from a dict
cash_flow_report_entity_from_dict = CashFlowReportEntity.from_dict(cash_flow_report_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


