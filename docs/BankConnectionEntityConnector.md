# BankConnectionEntityConnector


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
**created_at** | **object** |  | 
**updated_at** | **object** |  | 

## Example

```python
from python_core_api_sdk.models.bank_connection_entity_connector import BankConnectionEntityConnector

# TODO update the JSON string below
json = "{}"
# create an instance of BankConnectionEntityConnector from a JSON string
bank_connection_entity_connector_instance = BankConnectionEntityConnector.from_json(json)
# print the JSON string representation of the object
print(BankConnectionEntityConnector.to_json())

# convert the object into a dict
bank_connection_entity_connector_dict = bank_connection_entity_connector_instance.to_dict()
# create an instance of BankConnectionEntityConnector from a dict
bank_connection_entity_connector_from_dict = BankConnectionEntityConnector.from_dict(bank_connection_entity_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


