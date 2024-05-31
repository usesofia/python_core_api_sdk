# CreditCardMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_number** | **float** |  | [optional] 
**total_installments** | **float** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**payee_mcc** | **float** |  | [optional] 
**card_number** | **str** |  | [optional] 
**bill_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.credit_card_metadata_dto import CreditCardMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardMetadataDto from a JSON string
credit_card_metadata_dto_instance = CreditCardMetadataDto.from_json(json)
# print the JSON string representation of the object
print(CreditCardMetadataDto.to_json())

# convert the object into a dict
credit_card_metadata_dto_dict = credit_card_metadata_dto_instance.to_dict()
# create an instance of CreditCardMetadataDto from a dict
credit_card_metadata_dto_from_dict = CreditCardMetadataDto.from_dict(credit_card_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


