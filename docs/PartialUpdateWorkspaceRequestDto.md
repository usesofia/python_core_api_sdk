# PartialUpdateWorkspaceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.partial_update_workspace_request_dto import PartialUpdateWorkspaceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUpdateWorkspaceRequestDto from a JSON string
partial_update_workspace_request_dto_instance = PartialUpdateWorkspaceRequestDto.from_json(json)
# print the JSON string representation of the object
print(PartialUpdateWorkspaceRequestDto.to_json())

# convert the object into a dict
partial_update_workspace_request_dto_dict = partial_update_workspace_request_dto_instance.to_dict()
# create an instance of PartialUpdateWorkspaceRequestDto from a dict
partial_update_workspace_request_dto_from_dict = PartialUpdateWorkspaceRequestDto.from_dict(partial_update_workspace_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


