# CashFlowByCategoryReportEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CashFlowByCategoryReportItemEntity]**](CashFlowByCategoryReportItemEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowByCategoryReportEntity from a JSON string
cash_flow_by_category_report_entity_instance = CashFlowByCategoryReportEntity.from_json(json)
# print the JSON string representation of the object
print(CashFlowByCategoryReportEntity.to_json())

# convert the object into a dict
cash_flow_by_category_report_entity_dict = cash_flow_by_category_report_entity_instance.to_dict()
# create an instance of CashFlowByCategoryReportEntity from a dict
cash_flow_by_category_report_entity_from_dict = CashFlowByCategoryReportEntity.from_dict(cash_flow_by_category_report_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


