# VerifyEmailVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**purpose** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.verify_email_verification_code_request_dto import VerifyEmailVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmailVerificationCodeRequestDto from a JSON string
verify_email_verification_code_request_dto_instance = VerifyEmailVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(VerifyEmailVerificationCodeRequestDto.to_json())

# convert the object into a dict
verify_email_verification_code_request_dto_dict = verify_email_verification_code_request_dto_instance.to_dict()
# create an instance of VerifyEmailVerificationCodeRequestDto from a dict
verify_email_verification_code_request_dto_from_dict = VerifyEmailVerificationCodeRequestDto.from_dict(verify_email_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


