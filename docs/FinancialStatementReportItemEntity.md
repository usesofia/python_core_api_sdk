# FinancialStatementReportItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**entries_category_data** | [**FinancialStatementeEntriesCategoryData**](FinancialStatementeEntriesCategoryData.md) |  | [optional] 
**outflows_category_data** | [**FinancialStatementOutlfowsCategoryData**](FinancialStatementOutlfowsCategoryData.md) |  | [optional] 
**outcome_data** | [**FinancialStatementOutcomeReportDataEntity**](FinancialStatementOutcomeReportDataEntity.md) |  | [optional] 

## Example

```python
from python_core_api_sdk.models.financial_statement_report_item_entity import FinancialStatementReportItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialStatementReportItemEntity from a JSON string
financial_statement_report_item_entity_instance = FinancialStatementReportItemEntity.from_json(json)
# print the JSON string representation of the object
print(FinancialStatementReportItemEntity.to_json())

# convert the object into a dict
financial_statement_report_item_entity_dict = financial_statement_report_item_entity_instance.to_dict()
# create an instance of FinancialStatementReportItemEntity from a dict
financial_statement_report_item_entity_from_dict = FinancialStatementReportItemEntity.from_dict(financial_statement_report_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


