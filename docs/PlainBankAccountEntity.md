# PlainBankAccountEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**bank_connection_id** | **str** |  | 
**provider** | **str** |  | 
**provider_account_id** | **str** |  | 
**type** | **str** |  | 
**enabled** | **bool** |  | 
**number** | **str** |  | 
**balance** | **float** |  | 
**currency_code** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.plain_bank_account_entity import PlainBankAccountEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PlainBankAccountEntity from a JSON string
plain_bank_account_entity_instance = PlainBankAccountEntity.from_json(json)
# print the JSON string representation of the object
print(PlainBankAccountEntity.to_json())

# convert the object into a dict
plain_bank_account_entity_dict = plain_bank_account_entity_instance.to_dict()
# create an instance of PlainBankAccountEntity from a dict
plain_bank_account_entity_from_dict = PlainBankAccountEntity.from_dict(plain_bank_account_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


