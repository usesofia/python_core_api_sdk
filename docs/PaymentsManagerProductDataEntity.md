# PaymentsManagerProductDataEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**prices** | [**List[PaymentsManagerProductPriceEntity]**](PaymentsManagerProductPriceEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.payments_manager_product_data_entity import PaymentsManagerProductDataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsManagerProductDataEntity from a JSON string
payments_manager_product_data_entity_instance = PaymentsManagerProductDataEntity.from_json(json)
# print the JSON string representation of the object
print(PaymentsManagerProductDataEntity.to_json())

# convert the object into a dict
payments_manager_product_data_entity_dict = payments_manager_product_data_entity_instance.to_dict()
# create an instance of PaymentsManagerProductDataEntity from a dict
payments_manager_product_data_entity_from_dict = PaymentsManagerProductDataEntity.from_dict(payments_manager_product_data_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


