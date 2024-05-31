# SignUpWithEmailPasswordRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**email_verification_code** | **str** |  | 

## Example

```python
from openapi_client.models.sign_up_with_email_password_request_dto import SignUpWithEmailPasswordRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpWithEmailPasswordRequestDto from a JSON string
sign_up_with_email_password_request_dto_instance = SignUpWithEmailPasswordRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignUpWithEmailPasswordRequestDto.to_json())

# convert the object into a dict
sign_up_with_email_password_request_dto_dict = sign_up_with_email_password_request_dto_instance.to_dict()
# create an instance of SignUpWithEmailPasswordRequestDto from a dict
sign_up_with_email_password_request_dto_from_dict = SignUpWithEmailPasswordRequestDto.from_dict(sign_up_with_email_password_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


