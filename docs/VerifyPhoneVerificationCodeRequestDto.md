# VerifyPhoneVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 
**purpose** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.verify_phone_verification_code_request_dto import VerifyPhoneVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPhoneVerificationCodeRequestDto from a JSON string
verify_phone_verification_code_request_dto_instance = VerifyPhoneVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(VerifyPhoneVerificationCodeRequestDto.to_json())

# convert the object into a dict
verify_phone_verification_code_request_dto_dict = verify_phone_verification_code_request_dto_instance.to_dict()
# create an instance of VerifyPhoneVerificationCodeRequestDto from a dict
verify_phone_verification_code_request_dto_from_dict = VerifyPhoneVerificationCodeRequestDto.from_dict(verify_phone_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


