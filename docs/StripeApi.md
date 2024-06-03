# python_core_api_sdk.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_controller_create_checkout_session_for_stripe**](StripeApi.md#stripe_controller_create_checkout_session_for_stripe) | **POST** /stripe/checkout-session | 
[**stripe_controller_stripe_webhook**](StripeApi.md#stripe_controller_stripe_webhook) | **POST** /stripe/webhook | 


# **stripe_controller_create_checkout_session_for_stripe**
> CheckoutSessionEntity stripe_controller_create_checkout_session_for_stripe(create_stripe_checkout_session_request_dto)



### Example


```python
import python_core_api_sdk
from python_core_api_sdk.models.checkout_session_entity import CheckoutSessionEntity
from python_core_api_sdk.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto
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
    api_instance = python_core_api_sdk.StripeApi(api_client)
    create_stripe_checkout_session_request_dto = python_core_api_sdk.CreateStripeCheckoutSessionRequestDto() # CreateStripeCheckoutSessionRequestDto | 

    try:
        api_response = await api_instance.stripe_controller_create_checkout_session_for_stripe(create_stripe_checkout_session_request_dto)
        print("The response of StripeApi->stripe_controller_create_checkout_session_for_stripe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_controller_create_checkout_session_for_stripe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stripe_checkout_session_request_dto** | [**CreateStripeCheckoutSessionRequestDto**](CreateStripeCheckoutSessionRequestDto.md)|  | 

### Return type

[**CheckoutSessionEntity**](CheckoutSessionEntity.md)

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

# **stripe_controller_stripe_webhook**
> stripe_controller_stripe_webhook(stripe_signature)



### Example


```python
import python_core_api_sdk
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
    api_instance = python_core_api_sdk.StripeApi(api_client)
    stripe_signature = 'stripe_signature_example' # str | 

    try:
        await api_instance.stripe_controller_stripe_webhook(stripe_signature)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_controller_stripe_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_signature** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

