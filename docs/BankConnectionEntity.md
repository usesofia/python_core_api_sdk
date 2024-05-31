# BankConnectionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_by_user_id** | **str** |  | 
**workspace_id** | **str** |  | 
**enabled** | **bool** |  | 
**provider** | **str** |  | 
**provider_item_id** | **str** |  | 
**history_range** | **str** |  | 
**connector_id** | **str** |  | 
**connector** | [**BankConnectorEntity**](BankConnectorEntity.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from openapi_client.models.bank_connection_entity import BankConnectionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankConnectionEntity from a JSON string
bank_connection_entity_instance = BankConnectionEntity.from_json(json)
# print the JSON string representation of the object
print(BankConnectionEntity.to_json())

# convert the object into a dict
bank_connection_entity_dict = bank_connection_entity_instance.to_dict()
# create an instance of BankConnectionEntity from a dict
bank_connection_entity_from_dict = BankConnectionEntity.from_dict(bank_connection_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


