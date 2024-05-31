# PaymentDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_name** | **str** |  | [optional] 
**payer_branch_number** | **str** |  | [optional] 
**payer_account_number** | **str** |  | [optional] 
**payer_routing_number** | **str** |  | [optional] 
**payer_routing_number_ispb** | **str** |  | [optional] 
**payer_document_number_type** | **str** |  | [optional] 
**payer_document_number_value** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**receiver_name** | **str** |  | [optional] 
**receiver_branch_number** | **str** |  | [optional] 
**receiver_account_number** | **str** |  | [optional] 
**receiver_routing_number** | **str** |  | [optional] 
**receiver_routing_number_ispb** | **str** |  | [optional] 
**receiver_document_number_type** | **str** |  | [optional] 
**receiver_document_number_value** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**receiver_reference_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_data_dto import PaymentDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDataDto from a JSON string
payment_data_dto_instance = PaymentDataDto.from_json(json)
# print the JSON string representation of the object
print(PaymentDataDto.to_json())

# convert the object into a dict
payment_data_dto_dict = payment_data_dto_instance.to_dict()
# create an instance of PaymentDataDto from a dict
payment_data_dto_from_dict = PaymentDataDto.from_dict(payment_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


