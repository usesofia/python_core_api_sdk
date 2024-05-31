# CreateStripeCheckoutSessionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**price_id** | **str** |  | 
**is_trial** | **bool** |  | 

## Example

```python
from python_core_api_sdk.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionRequestDto from a JSON string
create_stripe_checkout_session_request_dto_instance = CreateStripeCheckoutSessionRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionRequestDto.to_json())

# convert the object into a dict
create_stripe_checkout_session_request_dto_dict = create_stripe_checkout_session_request_dto_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionRequestDto from a dict
create_stripe_checkout_session_request_dto_from_dict = CreateStripeCheckoutSessionRequestDto.from_dict(create_stripe_checkout_session_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


