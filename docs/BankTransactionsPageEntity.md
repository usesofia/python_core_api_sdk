# BankTransactionsPageEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_index** | **float** |  | 
**page_size** | **float** |  | 
**total_items** | **float** |  | 
**total_pages** | **float** |  | 
**items** | [**List[BankTransactionEntity]**](BankTransactionEntity.md) |  | 

## Example

```python
from openapi_client.models.bank_transactions_page_entity import BankTransactionsPageEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankTransactionsPageEntity from a JSON string
bank_transactions_page_entity_instance = BankTransactionsPageEntity.from_json(json)
# print the JSON string representation of the object
print(BankTransactionsPageEntity.to_json())

# convert the object into a dict
bank_transactions_page_entity_dict = bank_transactions_page_entity_instance.to_dict()
# create an instance of BankTransactionsPageEntity from a dict
bank_transactions_page_entity_from_dict = BankTransactionsPageEntity.from_dict(bank_transactions_page_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


