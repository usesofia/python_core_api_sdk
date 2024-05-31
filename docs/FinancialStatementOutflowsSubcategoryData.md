# FinancialStatementOutflowsSubcategoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subcategory_id** | **str** |  | 
**subcategory_name** | **str** |  | 
**outcome** | **float** |  | 

## Example

```python
from python_core_api_sdk.models.financial_statement_outflows_subcategory_data import FinancialStatementOutflowsSubcategoryData

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialStatementOutflowsSubcategoryData from a JSON string
financial_statement_outflows_subcategory_data_instance = FinancialStatementOutflowsSubcategoryData.from_json(json)
# print the JSON string representation of the object
print(FinancialStatementOutflowsSubcategoryData.to_json())

# convert the object into a dict
financial_statement_outflows_subcategory_data_dict = financial_statement_outflows_subcategory_data_instance.to_dict()
# create an instance of FinancialStatementOutflowsSubcategoryData from a dict
financial_statement_outflows_subcategory_data_from_dict = FinancialStatementOutflowsSubcategoryData.from_dict(financial_statement_outflows_subcategory_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


