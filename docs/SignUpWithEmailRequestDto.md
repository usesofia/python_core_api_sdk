# SignUpWithEmailRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**phone** | **str** |  | 
**password** | **str** |  | 
**email_verification_code** | **str** |  | 
**phone_verification_code** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.sign_up_with_email_request_dto import SignUpWithEmailRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpWithEmailRequestDto from a JSON string
sign_up_with_email_request_dto_instance = SignUpWithEmailRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignUpWithEmailRequestDto.to_json())

# convert the object into a dict
sign_up_with_email_request_dto_dict = sign_up_with_email_request_dto_instance.to_dict()
# create an instance of SignUpWithEmailRequestDto from a dict
sign_up_with_email_request_dto_from_dict = SignUpWithEmailRequestDto.from_dict(sign_up_with_email_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


