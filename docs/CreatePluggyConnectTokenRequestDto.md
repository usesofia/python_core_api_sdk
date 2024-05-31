# CreatePluggyConnectTokenRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | 
**history_range** | **str** |  | 

## Example

```python
from openapi_client.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePluggyConnectTokenRequestDto from a JSON string
create_pluggy_connect_token_request_dto_instance = CreatePluggyConnectTokenRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreatePluggyConnectTokenRequestDto.to_json())

# convert the object into a dict
create_pluggy_connect_token_request_dto_dict = create_pluggy_connect_token_request_dto_instance.to_dict()
# create an instance of CreatePluggyConnectTokenRequestDto from a dict
create_pluggy_connect_token_request_dto_from_dict = CreatePluggyConnectTokenRequestDto.from_dict(create_pluggy_connect_token_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


