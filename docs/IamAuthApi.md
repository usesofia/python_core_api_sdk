# python_core_api_sdk.IamAuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_generate_and_send_email_verification_code**](IamAuthApi.md#auth_controller_generate_and_send_email_verification_code) | **POST** /iam/auth/email-verification-code | 
[**auth_controller_generate_and_send_phone_verification_code**](IamAuthApi.md#auth_controller_generate_and_send_phone_verification_code) | **POST** /iam/auth/phone-verification-code | 
[**auth_controller_sign_in_with_email**](IamAuthApi.md#auth_controller_sign_in_with_email) | **POST** /iam/auth/sign-in/email | 
[**auth_controller_sign_up_with_email**](IamAuthApi.md#auth_controller_sign_up_with_email) | **POST** /iam/auth/sign-up/email | 
[**auth_controller_verify_email_verification_code**](IamAuthApi.md#auth_controller_verify_email_verification_code) | **GET** /iam/auth/email-verification-code/verify | 
[**auth_controller_verify_phone_verification_code**](IamAuthApi.md#auth_controller_verify_phone_verification_code) | **GET** /iam/auth/phone-verification-code/verify | 


# **auth_controller_generate_and_send_email_verification_code**
> auth_controller_generate_and_send_email_verification_code(generate_and_send_email_verification_code_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.generate_and_send_email_verification_code_request_dto import GenerateAndSendEmailVerificationCodeRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    generate_and_send_email_verification_code_request_dto = python_core_api_sdk.GenerateAndSendEmailVerificationCodeRequestDto() # GenerateAndSendEmailVerificationCodeRequestDto | 

    try:
        await api_instance.auth_controller_generate_and_send_email_verification_code(generate_and_send_email_verification_code_request_dto)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_generate_and_send_email_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_and_send_email_verification_code_request_dto** | [**GenerateAndSendEmailVerificationCodeRequestDto**](GenerateAndSendEmailVerificationCodeRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_generate_and_send_phone_verification_code**
> auth_controller_generate_and_send_phone_verification_code(generate_and_send_phone_verification_code_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.generate_and_send_phone_verification_code_request_dto import GenerateAndSendPhoneVerificationCodeRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    generate_and_send_phone_verification_code_request_dto = python_core_api_sdk.GenerateAndSendPhoneVerificationCodeRequestDto() # GenerateAndSendPhoneVerificationCodeRequestDto | 

    try:
        await api_instance.auth_controller_generate_and_send_phone_verification_code(generate_and_send_phone_verification_code_request_dto)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_generate_and_send_phone_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_and_send_phone_verification_code_request_dto** | [**GenerateAndSendPhoneVerificationCodeRequestDto**](GenerateAndSendPhoneVerificationCodeRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_sign_in_with_email**
> CredentialsEntity auth_controller_sign_in_with_email(sign_in_with_email_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.sign_in_with_email_request_dto import SignInWithEmailRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    sign_in_with_email_request_dto = python_core_api_sdk.SignInWithEmailRequestDto() # SignInWithEmailRequestDto | 

    try:
        api_response = await api_instance.auth_controller_sign_in_with_email(sign_in_with_email_request_dto)
        print("The response of IamAuthApi->auth_controller_sign_in_with_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_sign_in_with_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_in_with_email_request_dto** | [**SignInWithEmailRequestDto**](SignInWithEmailRequestDto.md)|  | 

### Return type

[**CredentialsEntity**](CredentialsEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_sign_up_with_email**
> UserEntity auth_controller_sign_up_with_email(sign_up_with_email_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sign_up_with_email_request_dto import SignUpWithEmailRequestDto
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    sign_up_with_email_request_dto = python_core_api_sdk.SignUpWithEmailRequestDto() # SignUpWithEmailRequestDto | 

    try:
        api_response = await api_instance.auth_controller_sign_up_with_email(sign_up_with_email_request_dto)
        print("The response of IamAuthApi->auth_controller_sign_up_with_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_sign_up_with_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_with_email_request_dto** | [**SignUpWithEmailRequestDto**](SignUpWithEmailRequestDto.md)|  | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_verify_email_verification_code**
> auth_controller_verify_email_verification_code(verify_email_verification_code_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.verify_email_verification_code_request_dto import VerifyEmailVerificationCodeRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    verify_email_verification_code_request_dto = python_core_api_sdk.VerifyEmailVerificationCodeRequestDto() # VerifyEmailVerificationCodeRequestDto | 

    try:
        await api_instance.auth_controller_verify_email_verification_code(verify_email_verification_code_request_dto)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_verify_email_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_email_verification_code_request_dto** | [**VerifyEmailVerificationCodeRequestDto**](VerifyEmailVerificationCodeRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_verify_phone_verification_code**
> auth_controller_verify_phone_verification_code(verify_phone_verification_code_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.verify_phone_verification_code_request_dto import VerifyPhoneVerificationCodeRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.IamAuthApi(api_client)
    verify_phone_verification_code_request_dto = python_core_api_sdk.VerifyPhoneVerificationCodeRequestDto() # VerifyPhoneVerificationCodeRequestDto | 

    try:
        await api_instance.auth_controller_verify_phone_verification_code(verify_phone_verification_code_request_dto)
    except Exception as e:
        print("Exception when calling IamAuthApi->auth_controller_verify_phone_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_phone_verification_code_request_dto** | [**VerifyPhoneVerificationCodeRequestDto**](VerifyPhoneVerificationCodeRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

