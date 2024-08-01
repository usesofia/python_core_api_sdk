# PartialUpdateBankTransactionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**competency_date** | **str** |  | [optional] 
**ignore** | **bool** |  | [optional] 
**verify** | **bool** |  | [optional] 
**tag_ids** | **List[str]** |  | [optional] 
**legal_nature** | **str** |  | [optional] 

## Example

```python
from python_core_api_sdk.models.partial_update_bank_transaction_request_dto import PartialUpdateBankTransactionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUpdateBankTransactionRequestDto from a JSON string
partial_update_bank_transaction_request_dto_instance = PartialUpdateBankTransactionRequestDto.from_json(json)
# print the JSON string representation of the object
print(PartialUpdateBankTransactionRequestDto.to_json())

# convert the object into a dict
partial_update_bank_transaction_request_dto_dict = partial_update_bank_transaction_request_dto_instance.to_dict()
# create an instance of PartialUpdateBankTransactionRequestDto from a dict
partial_update_bank_transaction_request_dto_from_dict = PartialUpdateBankTransactionRequestDto.from_dict(partial_update_bank_transaction_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


