# CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata


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
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata from a JSON string
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata_instance = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.to_json())

# convert the object into a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata_dict = create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata_instance.to_dict()
# create an instance of CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata from a dict
create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata_from_dict = CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.from_dict(create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


