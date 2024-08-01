# CreateOrUpdateBankAccountRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_connection_id** | **str** |  | 
**provider** | **str** |  | 
**provider_account_id** | **str** |  | 
**type** | **str** |  | 
**number** | **str** |  | 
**balance** | **int** |  | 
**currency_code** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankAccountRequestDto from a JSON string
create_or_update_bank_account_request_dto_instance = CreateOrUpdateBankAccountRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankAccountRequestDto.to_json())

# convert the object into a dict
create_or_update_bank_account_request_dto_dict = create_or_update_bank_account_request_dto_instance.to_dict()
# create an instance of CreateOrUpdateBankAccountRequestDto from a dict
create_or_update_bank_account_request_dto_from_dict = CreateOrUpdateBankAccountRequestDto.from_dict(create_or_update_bank_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


