# CashFlowReportDailyItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | 
**var_date** | **datetime** |  | 
**day_of_year** | **float** |  | 
**label** | **str** |  | 
**min_date** | **datetime** |  | 
**max_date** | **datetime** |  | 
**value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cash_flow_report_daily_item_entity import CashFlowReportDailyItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowReportDailyItemEntity from a JSON string
cash_flow_report_daily_item_entity_instance = CashFlowReportDailyItemEntity.from_json(json)
# print the JSON string representation of the object
print(CashFlowReportDailyItemEntity.to_json())

# convert the object into a dict
cash_flow_report_daily_item_entity_dict = cash_flow_report_daily_item_entity_instance.to_dict()
# create an instance of CashFlowReportDailyItemEntity from a dict
cash_flow_report_daily_item_entity_from_dict = CashFlowReportDailyItemEntity.from_dict(cash_flow_report_daily_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


