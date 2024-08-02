# BankTransactionsPageEntityItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**account** | [**BankConnectionEntityAccountsInner**](BankConnectionEntityAccountsInner.md) |  | 
**workspace_id** | **str** |  | 
**provider** | **str** |  | 
**provider_transaction_id** | **str** |  | 
**original_description** | **str** |  | 
**description** | **str** |  | 
**posted_date** | **datetime** |  | 
**competency_date** | **datetime** |  | 
**amount** | **int** |  | 
**direction_nature** | **str** |  | 
**status** | **str** |  | 
**legal_nature** | **str** |  | 
**provider_category_id** | **str** |  | [optional] 
**provider_category_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category** | [**BankTransactionEntityCategory**](BankTransactionEntityCategory.md) |  | [optional] 
**tags** | [**List[BankTransactionEntityTagsInner]**](BankTransactionEntityTagsInner.md) |  | 
**payment_data_id** | **str** |  | [optional] 
**payment_data** | [**BankTransactionEntityPaymentData**](BankTransactionEntityPaymentData.md) |  | [optional] 
**credit_card_metadata_id** | **str** |  | [optional] 
**credit_card_metadata** | [**BankTransactionEntityCreditCardMetadata**](BankTransactionEntityCreditCardMetadata.md) |  | [optional] 
**ignored_at** | **datetime** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transactions_page_entity_items_inner import BankTransactionsPageEntityItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionsPageEntityItemsInner from a JSON string
bank_transactions_page_entity_items_inner_instance = BankTransactionsPageEntityItemsInner.from_json(json)
# print the JSON string representation of the object
print(BankTransactionsPageEntityItemsInner.to_json())

# convert the object into a dict
bank_transactions_page_entity_items_inner_dict = bank_transactions_page_entity_items_inner_instance.to_dict()
# create an instance of BankTransactionsPageEntityItemsInner from a dict
bank_transactions_page_entity_items_inner_from_dict = BankTransactionsPageEntityItemsInner.from_dict(bank_transactions_page_entity_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


