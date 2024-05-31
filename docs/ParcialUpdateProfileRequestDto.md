# ParcialUpdateProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**birth_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.parcial_update_profile_request_dto import ParcialUpdateProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ParcialUpdateProfileRequestDto from a JSON string
parcial_update_profile_request_dto_instance = ParcialUpdateProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ParcialUpdateProfileRequestDto.to_json())

# convert the object into a dict
parcial_update_profile_request_dto_dict = parcial_update_profile_request_dto_instance.to_dict()
# create an instance of ParcialUpdateProfileRequestDto from a dict
parcial_update_profile_request_dto_from_dict = ParcialUpdateProfileRequestDto.from_dict(parcial_update_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


