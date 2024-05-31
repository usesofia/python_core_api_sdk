# FinancialStatementeEntriesCategoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | 
**category_name** | **str** |  | 
**outcome** | **float** |  | 
**subcategories** | [**List[FinancialStatementeEntriesSubcategoryData]**](FinancialStatementeEntriesSubcategoryData.md) |  | 

## Example

```python
from openapi_client.models.financial_statemente_entries_category_data import FinancialStatementeEntriesCategoryData

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialStatementeEntriesCategoryData from a JSON string
financial_statemente_entries_category_data_instance = FinancialStatementeEntriesCategoryData.from_json(json)
# print the JSON string representation of the object
print(FinancialStatementeEntriesCategoryData.to_json())

# convert the object into a dict
financial_statemente_entries_category_data_dict = financial_statemente_entries_category_data_instance.to_dict()
# create an instance of FinancialStatementeEntriesCategoryData from a dict
financial_statemente_entries_category_data_from_dict = FinancialStatementeEntriesCategoryData.from_dict(financial_statemente_entries_category_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


