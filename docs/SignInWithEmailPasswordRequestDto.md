# SignInWithEmailPasswordRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**client_id** | **str** |  | 

## Example

```python
from openapi_client.models.sign_in_with_email_password_request_dto import SignInWithEmailPasswordRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignInWithEmailPasswordRequestDto from a JSON string
sign_in_with_email_password_request_dto_instance = SignInWithEmailPasswordRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignInWithEmailPasswordRequestDto.to_json())

# convert the object into a dict
sign_in_with_email_password_request_dto_dict = sign_in_with_email_password_request_dto_instance.to_dict()
# create an instance of SignInWithEmailPasswordRequestDto from a dict
sign_in_with_email_password_request_dto_from_dict = SignInWithEmailPasswordRequestDto.from_dict(sign_in_with_email_password_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


