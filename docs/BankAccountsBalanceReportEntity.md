# BankAccountsBalanceReportEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BankAccountsBalanceReportEntityItemsInner]**](BankAccountsBalanceReportEntityItemsInner.md) |  | 
**bank_accounts** | [**List[BankConnectionEntityAccountsInner]**](BankConnectionEntityAccountsInner.md) |  | 

## Example

```python
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountsBalanceReportEntity from a JSON string
bank_accounts_balance_report_entity_instance = BankAccountsBalanceReportEntity.from_json(json)
# print the JSON string representation of the object
print(BankAccountsBalanceReportEntity.to_json())

# convert the object into a dict
bank_accounts_balance_report_entity_dict = bank_accounts_balance_report_entity_instance.to_dict()
# create an instance of BankAccountsBalanceReportEntity from a dict
bank_accounts_balance_report_entity_from_dict = BankAccountsBalanceReportEntity.from_dict(bank_accounts_balance_report_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


