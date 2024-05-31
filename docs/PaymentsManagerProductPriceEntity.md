# PaymentsManagerProductPriceEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**active** | **bool** |  | 
**unit_amount** | **float** |  | 
**interval** | **str** |  | 

## Example

```python
from openapi_client.models.payments_manager_product_price_entity import PaymentsManagerProductPriceEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsManagerProductPriceEntity from a JSON string
payments_manager_product_price_entity_instance = PaymentsManagerProductPriceEntity.from_json(json)
# print the JSON string representation of the object
print(PaymentsManagerProductPriceEntity.to_json())

# convert the object into a dict
payments_manager_product_price_entity_dict = payments_manager_product_price_entity_instance.to_dict()
# create an instance of PaymentsManagerProductPriceEntity from a dict
payments_manager_product_price_entity_from_dict = PaymentsManagerProductPriceEntity.from_dict(payments_manager_product_price_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


