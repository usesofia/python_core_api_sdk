# CreateOrUpdateMessageTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | 
**device_id** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateMessageTokenRequestDto from a JSON string
create_or_update_message_token_request_dto_instance = CreateOrUpdateMessageTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateMessageTokenRequestDto.to_json())

# convert the object into a dict
create_or_update_message_token_request_dto_dict = create_or_update_message_token_request_dto_instance.to_dict()
# create an instance of CreateOrUpdateMessageTokenRequestDto from a dict
create_or_update_message_token_request_dto_from_dict = CreateOrUpdateMessageTokenRequestDto.from_dict(create_or_update_message_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


