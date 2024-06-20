# GenerateAndSendEmailVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**purpose** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.generate_and_send_email_verification_code_request_dto import GenerateAndSendEmailVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAndSendEmailVerificationCodeRequestDto from a JSON string
generate_and_send_email_verification_code_request_dto_instance = GenerateAndSendEmailVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(GenerateAndSendEmailVerificationCodeRequestDto.to_json())

# convert the object into a dict
generate_and_send_email_verification_code_request_dto_dict = generate_and_send_email_verification_code_request_dto_instance.to_dict()
# create an instance of GenerateAndSendEmailVerificationCodeRequestDto from a dict
generate_and_send_email_verification_code_request_dto_from_dict = GenerateAndSendEmailVerificationCodeRequestDto.from_dict(generate_and_send_email_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


