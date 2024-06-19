# SendPhoneVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.send_phone_verification_code_request_dto import SendPhoneVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SendPhoneVerificationCodeRequestDto from a JSON string
send_phone_verification_code_request_dto_instance = SendPhoneVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(SendPhoneVerificationCodeRequestDto.to_json())

# convert the object into a dict
send_phone_verification_code_request_dto_dict = send_phone_verification_code_request_dto_instance.to_dict()
# create an instance of SendPhoneVerificationCodeRequestDto from a dict
send_phone_verification_code_request_dto_from_dict = SendPhoneVerificationCodeRequestDto.from_dict(send_phone_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


