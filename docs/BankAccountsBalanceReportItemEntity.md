# BankAccountsBalanceReportItemEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_balance** | **float** |  | 
**currency_code** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.bank_accounts_balance_report_item_entity import BankAccountsBalanceReportItemEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountsBalanceReportItemEntity from a JSON string
bank_accounts_balance_report_item_entity_instance = BankAccountsBalanceReportItemEntity.from_json(json)
# print the JSON string representation of the object
print(BankAccountsBalanceReportItemEntity.to_json())

# convert the object into a dict
bank_accounts_balance_report_item_entity_dict = bank_accounts_balance_report_item_entity_instance.to_dict()
# create an instance of BankAccountsBalanceReportItemEntity from a dict
bank_accounts_balance_report_item_entity_from_dict = BankAccountsBalanceReportItemEntity.from_dict(bank_accounts_balance_report_item_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


