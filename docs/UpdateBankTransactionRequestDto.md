# UpdateBankTransactionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**competency_date** | **datetime** |  | [optional] 
**ignore** | **bool** |  | [optional] 
**confirm** | **bool** |  | [optional] 
**tag_ids** | **List[str]** |  | [optional] 
**legal_nature** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_bank_transaction_request_dto import UpdateBankTransactionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBankTransactionRequestDto from a JSON string
update_bank_transaction_request_dto_instance = UpdateBankTransactionRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateBankTransactionRequestDto.to_json())

# convert the object into a dict
update_bank_transaction_request_dto_dict = update_bank_transaction_request_dto_instance.to_dict()
# create an instance of UpdateBankTransactionRequestDto from a dict
update_bank_transaction_request_dto_from_dict = UpdateBankTransactionRequestDto.from_dict(update_bank_transaction_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


