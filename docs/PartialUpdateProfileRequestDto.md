# PartialUpdateProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**birth_date** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.partial_update_profile_request_dto import PartialUpdateProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUpdateProfileRequestDto from a JSON string
partial_update_profile_request_dto_instance = PartialUpdateProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(PartialUpdateProfileRequestDto.to_json())

# convert the object into a dict
partial_update_profile_request_dto_dict = partial_update_profile_request_dto_instance.to_dict()
# create an instance of PartialUpdateProfileRequestDto from a dict
partial_update_profile_request_dto_from_dict = PartialUpdateProfileRequestDto.from_dict(partial_update_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


