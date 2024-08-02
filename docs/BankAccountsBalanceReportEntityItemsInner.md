# BankAccountsBalanceReportEntityItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_balance** | **int** |  | 
**currency_code** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.bank_accounts_balance_report_entity_items_inner import BankAccountsBalanceReportEntityItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountsBalanceReportEntityItemsInner from a JSON string
bank_accounts_balance_report_entity_items_inner_instance = BankAccountsBalanceReportEntityItemsInner.from_json(json)
# print the JSON string representation of the object
print(BankAccountsBalanceReportEntityItemsInner.to_json())

# convert the object into a dict
bank_accounts_balance_report_entity_items_inner_dict = bank_accounts_balance_report_entity_items_inner_instance.to_dict()
# create an instance of BankAccountsBalanceReportEntityItemsInner from a dict
bank_accounts_balance_report_entity_items_inner_from_dict = BankAccountsBalanceReportEntityItemsInner.from_dict(bank_accounts_balance_report_entity_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


