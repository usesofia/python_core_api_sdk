# CreateProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**birth_date** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileRequestDto from a JSON string
create_profile_request_dto_instance = CreateProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateProfileRequestDto.to_json())

# convert the object into a dict
create_profile_request_dto_dict = create_profile_request_dto_instance.to_dict()
# create an instance of CreateProfileRequestDto from a dict
create_profile_request_dto_from_dict = CreateProfileRequestDto.from_dict(create_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


