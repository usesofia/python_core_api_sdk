# CashFlowReportMonthlyItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | 
**var_date** | **datetime** |  | 
**month** | **float** |  | 
**label** | **str** |  | 
**min_date** | **datetime** |  | 
**max_date** | **datetime** |  | 
**value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.cash_flow_report_monthly_item_entity import CashFlowReportMonthlyItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowReportMonthlyItemEntity from a JSON string
cash_flow_report_monthly_item_entity_instance = CashFlowReportMonthlyItemEntity.from_json(json)
# print the JSON string representation of the object
print(CashFlowReportMonthlyItemEntity.to_json())

# convert the object into a dict
cash_flow_report_monthly_item_entity_dict = cash_flow_report_monthly_item_entity_instance.to_dict()
# create an instance of CashFlowReportMonthlyItemEntity from a dict
cash_flow_report_monthly_item_entity_from_dict = CashFlowReportMonthlyItemEntity.from_dict(cash_flow_report_monthly_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


