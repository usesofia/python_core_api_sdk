# FinancialStatementOutlfowsCategoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | 
**category_name** | **str** |  | 
**outcome** | **float** |  | 
**subcategories** | [**List[FinancialStatementOutflowsSubcategoryData]**](FinancialStatementOutflowsSubcategoryData.md) |  | 

## Example

```python
from python_core_api_sdk.models.financial_statement_outlfows_category_data import FinancialStatementOutlfowsCategoryData

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialStatementOutlfowsCategoryData from a JSON string
financial_statement_outlfows_category_data_instance = FinancialStatementOutlfowsCategoryData.from_json(json)
# print the JSON string representation of the object
print(FinancialStatementOutlfowsCategoryData.to_json())

# convert the object into a dict
financial_statement_outlfows_category_data_dict = financial_statement_outlfows_category_data_instance.to_dict()
# create an instance of FinancialStatementOutlfowsCategoryData from a dict
financial_statement_outlfows_category_data_from_dict = FinancialStatementOutlfowsCategoryData.from_dict(financial_statement_outlfows_category_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


