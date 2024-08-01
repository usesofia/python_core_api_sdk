# CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**provider** | **str** |  | 
**workspace_id** | **str** |  | 
**provider_transaction_id** | **str** |  | 
**description** | **str** |  | 
**posted_date** | **object** |  | 
**competency_date** | **object** |  | 
**amount** | **float** |  | 
**direction_nature** | **str** |  | 
**status** | **str** |  | 
**legal_nature** | **str** |  | 
**provider_category_id** | **str** |  | [optional] 
**provider_category_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**payment_data** | [**CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData**](CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.md) |  | [optional] 
**credit_card_metadata** | [**CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata**](CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.md) |  | [optional] 
**category_guesses** | [**List[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner]**](CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner.md) |  | [optional] 
**legal_nature_guesses** | [**List[CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner]**](CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner.md) |  | [optional] 

## Example

```python
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner from a JSON string
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_instance = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner.to_json())

# convert the object into a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_dict = create_or_update_bank_transactions_in_bulk_request_dto_items_inner_instance.to_dict()
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner from a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_from_dict = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner.from_dict(create_or_update_bank_transactions_in_bulk_request_dto_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


