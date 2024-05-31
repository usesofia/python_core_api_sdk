# CreateOrUpdateBankTransactionsInBulkRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateOrUpdateBankTransactionsInBulkItemDto]**](CreateOrUpdateBankTransactionsInBulkItemDto.md) |  | 

## Example

```python
from openapi_client.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDto from a JSON string
create_or_update_bank_transactions_in_bulk_request_dto_instance = CreateOrUpdateBankTransactionsInBulkRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankTransactionsInBulkRequestDto.to_json())

# convert the object into a dict
create_or_update_bank_transactions_in_bulk_request_dto_dict = create_or_update_bank_transactions_in_bulk_request_dto_instance.to_dict()
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDto from a dict
create_or_update_bank_transactions_in_bulk_request_dto_from_dict = CreateOrUpdateBankTransactionsInBulkRequestDto.from_dict(create_or_update_bank_transactions_in_bulk_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


