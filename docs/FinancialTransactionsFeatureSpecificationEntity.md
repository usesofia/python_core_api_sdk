# FinancialTransactionsFeatureSpecificationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**unlimited** | **bool** |  | 
**max_per_month** | **float** |  | [optional] 
**subscription_product_id** | **str** |  | 

## Example

```python
from openapi_client.models.financial_transactions_feature_specification_entity import FinancialTransactionsFeatureSpecificationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialTransactionsFeatureSpecificationEntity from a JSON string
financial_transactions_feature_specification_entity_instance = FinancialTransactionsFeatureSpecificationEntity.from_json(json)
# print the JSON string representation of the object
print(FinancialTransactionsFeatureSpecificationEntity.to_json())

# convert the object into a dict
financial_transactions_feature_specification_entity_dict = financial_transactions_feature_specification_entity_instance.to_dict()
# create an instance of FinancialTransactionsFeatureSpecificationEntity from a dict
financial_transactions_feature_specification_entity_from_dict = FinancialTransactionsFeatureSpecificationEntity.from_dict(financial_transactions_feature_specification_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


