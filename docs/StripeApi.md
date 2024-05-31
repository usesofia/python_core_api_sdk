# openapi_client.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_controller_create_checkout_session_for_stripe**](StripeApi.md#stripe_controller_create_checkout_session_for_stripe) | **POST** /stripe/checkout-session | 
[**stripe_controller_stripe_webhook**](StripeApi.md#stripe_controller_stripe_webhook) | **POST** /stripe/webhook | 


# **stripe_controller_create_checkout_session_for_stripe**
> CheckoutSessionEntity stripe_controller_create_checkout_session_for_stripe(create_stripe_checkout_session_request_dto)



### Example


```python
import openapi_client
from openapi_client.models.checkout_session_entity import CheckoutSessionEntity
from openapi_client.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StripeApi(api_client)
    create_stripe_checkout_session_request_dto = openapi_client.CreateStripeCheckoutSessionRequestDto() # CreateStripeCheckoutSessionRequestDto | 

    try:
        api_response = api_instance.stripe_controller_create_checkout_session_for_stripe(create_stripe_checkout_session_request_dto)
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
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StripeApi(api_client)
    stripe_signature = 'stripe_signature_example' # str | 

    try:
        api_instance.stripe_controller_stripe_webhook(stripe_signature)
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

