# SendEmailVerificationCodeRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from openapi_client.models.send_email_verification_code_request_dto import SendEmailVerificationCodeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailVerificationCodeRequestDto from a JSON string
send_email_verification_code_request_dto_instance = SendEmailVerificationCodeRequestDto.from_json(json)
# print the JSON string representation of the object
print(SendEmailVerificationCodeRequestDto.to_json())

# convert the object into a dict
send_email_verification_code_request_dto_dict = send_email_verification_code_request_dto_instance.to_dict()
# create an instance of SendEmailVerificationCodeRequestDto from a dict
send_email_verification_code_request_dto_from_dict = SendEmailVerificationCodeRequestDto.from_dict(send_email_verification_code_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


