# CashFlowByCategoryReportItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | 
**category_name** | **str** |  | 
**absolute_value** | **float** |  | 
**percentage** | **float** |  | 

## Example

```python
from openapi_client.models.cash_flow_by_category_report_item_entity import CashFlowByCategoryReportItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowByCategoryReportItemEntity from a JSON string
cash_flow_by_category_report_item_entity_instance = CashFlowByCategoryReportItemEntity.from_json(json)
# print the JSON string representation of the object
print(CashFlowByCategoryReportItemEntity.to_json())

# convert the object into a dict
cash_flow_by_category_report_item_entity_dict = cash_flow_by_category_report_item_entity_instance.to_dict()
# create an instance of CashFlowByCategoryReportItemEntity from a dict
cash_flow_by_category_report_item_entity_from_dict = CashFlowByCategoryReportItemEntity.from_dict(cash_flow_by_category_report_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


