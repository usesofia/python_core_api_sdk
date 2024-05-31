# CreateOrUpdateBankTransactionsInBulkItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**provider** | **str** |  | 
**workspace_id** | **str** |  | 
**provider_transaction_id** | **str** |  | 
**description** | **str** |  | 
**posted_date** | **datetime** |  | 
**competency_date** | **datetime** |  | 
**amount** | **float** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**legal_nature** | **str** |  | 
**provider_category_id** | **str** |  | [optional] 
**provider_category_name** | **str** |  | [optional] 
**category_id** | **str** |  | 
**payment_data** | [**PaymentDataDto**](PaymentDataDto.md) |  | 
**credit_card_metadata** | [**CreditCardMetadataDto**](CreditCardMetadataDto.md) |  | 
**category_guesses** | [**List[CategoryGuessDto]**](CategoryGuessDto.md) |  | 
**best_guess_category_id** | **str** |  | 

## Example

```python
from openapi_client.models.create_or_update_bank_transactions_in_bulk_item_dto import CreateOrUpdateBankTransactionsInBulkItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankTransactionsInBulkItemDto from a JSON string
create_or_update_bank_transactions_in_bulk_item_dto_instance = CreateOrUpdateBankTransactionsInBulkItemDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankTransactionsInBulkItemDto.to_json())

# convert the object into a dict
create_or_update_bank_transactions_in_bulk_item_dto_dict = create_or_update_bank_transactions_in_bulk_item_dto_instance.to_dict()
# create an instance of CreateOrUpdateBankTransactionsInBulkItemDto from a dict
create_or_update_bank_transactions_in_bulk_item_dto_from_dict = CreateOrUpdateBankTransactionsInBulkItemDto.from_dict(create_or_update_bank_transactions_in_bulk_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


