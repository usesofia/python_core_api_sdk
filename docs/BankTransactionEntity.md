# BankTransactionEntity


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
**posted_date** | **object** |  | 
**competency_date** | **object** |  | 
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
**ignored_at** | **object** |  | [optional] 
**verified_at** | **object** |  | [optional] 
**created_at** | **object** |  | 
**updated_at** | **object** |  | 

## Example

```python
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionEntity from a JSON string
bank_transaction_entity_instance = BankTransactionEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionEntity.to_json())

# convert the object into a dict
bank_transaction_entity_dict = bank_transaction_entity_instance.to_dict()
# create an instance of BankTransactionEntity from a dict
bank_transaction_entity_from_dict = BankTransactionEntity.from_dict(bank_transaction_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


