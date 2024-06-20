# GenerateAndSendPhoneVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 
**purpose** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.generate_and_send_phone_verification_code_request_dto import GenerateAndSendPhoneVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAndSendPhoneVerificationCodeRequestDto from a JSON string
generate_and_send_phone_verification_code_request_dto_instance = GenerateAndSendPhoneVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(GenerateAndSendPhoneVerificationCodeRequestDto.to_json())

# convert the object into a dict
generate_and_send_phone_verification_code_request_dto_dict = generate_and_send_phone_verification_code_request_dto_instance.to_dict()
# create an instance of GenerateAndSendPhoneVerificationCodeRequestDto from a dict
generate_and_send_phone_verification_code_request_dto_from_dict = GenerateAndSendPhoneVerificationCodeRequestDto.from_dict(generate_and_send_phone_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


