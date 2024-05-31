# CreateOrUpdateBankConnectionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_id** | **str** |  | 
**provider** | **str** |  | 
**provider_item_id** | **str** |  | 
**provider_connector_id** | **str** |  | 
**history_range** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankConnectionRequestDto from a JSON string
create_or_update_bank_connection_request_dto_instance = CreateOrUpdateBankConnectionRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankConnectionRequestDto.to_json())

# convert the object into a dict
create_or_update_bank_connection_request_dto_dict = create_or_update_bank_connection_request_dto_instance.to_dict()
# create an instance of CreateOrUpdateBankConnectionRequestDto from a dict
create_or_update_bank_connection_request_dto_from_dict = CreateOrUpdateBankConnectionRequestDto.from_dict(create_or_update_bank_connection_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


