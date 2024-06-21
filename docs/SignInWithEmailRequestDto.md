# SignInWithEmailRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**client_id** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.sign_in_with_email_request_dto import SignInWithEmailRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignInWithEmailRequestDto from a JSON string
sign_in_with_email_request_dto_instance = SignInWithEmailRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignInWithEmailRequestDto.to_json())

# convert the object into a dict
sign_in_with_email_request_dto_dict = sign_in_with_email_request_dto_instance.to_dict()
# create an instance of SignInWithEmailRequestDto from a dict
sign_in_with_email_request_dto_from_dict = SignInWithEmailRequestDto.from_dict(sign_in_with_email_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


