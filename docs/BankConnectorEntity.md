# BankConnectorEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**provider** | **str** |  | 
**name** | **str** |  | 
**institution_url** | **str** |  | 
**image_url** | **str** |  | 
**primary_color** | **str** |  | 
**type** | **str** |  | 
**country** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.bank_connector_entity import BankConnectorEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankConnectorEntity from a JSON string
bank_connector_entity_instance = BankConnectorEntity.from_json(json)
# print the JSON string representation of the object
print(BankConnectorEntity.to_json())

# convert the object into a dict
bank_connector_entity_dict = bank_connector_entity_instance.to_dict()
# create an instance of BankConnectorEntity from a dict
bank_connector_entity_from_dict = BankConnectorEntity.from_dict(bank_connector_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


