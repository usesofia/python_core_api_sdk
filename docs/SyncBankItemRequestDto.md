# SyncBankItemRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_item_id** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_item_request_dto import SyncBankItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankItemRequestDto from a JSON string
sync_bank_item_request_dto_instance = SyncBankItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(SyncBankItemRequestDto.to_json())

# convert the object into a dict
sync_bank_item_request_dto_dict = sync_bank_item_request_dto_instance.to_dict()
# create an instance of SyncBankItemRequestDto from a dict
sync_bank_item_request_dto_from_dict = SyncBankItemRequestDto.from_dict(sync_bank_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


