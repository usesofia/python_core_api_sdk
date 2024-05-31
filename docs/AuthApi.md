# python_core_api_sdk.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_check_email_in_use**](AuthApi.md#auth_controller_check_email_in_use) | **POST** /auth/check-email-in-use | 
[**auth_controller_refresh**](AuthApi.md#auth_controller_refresh) | **POST** /auth/refresh | 
[**auth_controller_send_email_verification_code**](AuthApi.md#auth_controller_send_email_verification_code) | **POST** /auth/sign-up/email-verification-code | 
[**auth_controller_sign_in_with_email_password**](AuthApi.md#auth_controller_sign_in_with_email_password) | **POST** /auth/sign-in/email-password | 
[**auth_controller_sign_up_with_email_password**](AuthApi.md#auth_controller_sign_up_with_email_password) | **POST** /auth/sign-up/email-password | 


# **auth_controller_check_email_in_use**
> EmailInUseEntity auth_controller_check_email_in_use(check_email_in_use_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.check_email_in_use_request_dto import CheckEmailInUseRequestDto
from python_core_api_sdk.models.email_in_use_entity import EmailInUseEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.AuthApi(api_client)
    check_email_in_use_request_dto = python_core_api_sdk.CheckEmailInUseRequestDto() # CheckEmailInUseRequestDto | 

    try:
        api_response = api_instance.auth_controller_check_email_in_use(check_email_in_use_request_dto)
        print("The response of AuthApi->auth_controller_check_email_in_use:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_check_email_in_use: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_email_in_use_request_dto** | [**CheckEmailInUseRequestDto**](CheckEmailInUseRequestDto.md)|  | 

### Return type

[**EmailInUseEntity**](EmailInUseEntity.md)

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

# **auth_controller_refresh**
> CredentialsEntity auth_controller_refresh(refresh_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.refresh_request_dto import RefreshRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.AuthApi(api_client)
    refresh_request_dto = python_core_api_sdk.RefreshRequestDto() # RefreshRequestDto | 

    try:
        api_response = api_instance.auth_controller_refresh(refresh_request_dto)
        print("The response of AuthApi->auth_controller_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_request_dto** | [**RefreshRequestDto**](RefreshRequestDto.md)|  | 

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

# **auth_controller_send_email_verification_code**
> auth_controller_send_email_verification_code(send_email_verification_code_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.send_email_verification_code_request_dto import SendEmailVerificationCodeRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.AuthApi(api_client)
    send_email_verification_code_request_dto = python_core_api_sdk.SendEmailVerificationCodeRequestDto() # SendEmailVerificationCodeRequestDto | 

    try:
        api_instance.auth_controller_send_email_verification_code(send_email_verification_code_request_dto)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_send_email_verification_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_verification_code_request_dto** | [**SendEmailVerificationCodeRequestDto**](SendEmailVerificationCodeRequestDto.md)|  | 

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

# **auth_controller_sign_in_with_email_password**
> CredentialsEntity auth_controller_sign_in_with_email_password(sign_in_with_email_password_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.sign_in_with_email_password_request_dto import SignInWithEmailPasswordRequestDto
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.AuthApi(api_client)
    sign_in_with_email_password_request_dto = python_core_api_sdk.SignInWithEmailPasswordRequestDto() # SignInWithEmailPasswordRequestDto | 

    try:
        api_response = api_instance.auth_controller_sign_in_with_email_password(sign_in_with_email_password_request_dto)
        print("The response of AuthApi->auth_controller_sign_in_with_email_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_sign_in_with_email_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_in_with_email_password_request_dto** | [**SignInWithEmailPasswordRequestDto**](SignInWithEmailPasswordRequestDto.md)|  | 

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

# **auth_controller_sign_up_with_email_password**
> UserEntity auth_controller_sign_up_with_email_password(sign_up_with_email_password_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.sign_up_with_email_password_request_dto import SignUpWithEmailPasswordRequestDto
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.AuthApi(api_client)
    sign_up_with_email_password_request_dto = python_core_api_sdk.SignUpWithEmailPasswordRequestDto() # SignUpWithEmailPasswordRequestDto | 

    try:
        api_response = api_instance.auth_controller_sign_up_with_email_password(sign_up_with_email_password_request_dto)
        print("The response of AuthApi->auth_controller_sign_up_with_email_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_sign_up_with_email_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_with_email_password_request_dto** | [**SignUpWithEmailPasswordRequestDto**](SignUpWithEmailPasswordRequestDto.md)|  | 

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

