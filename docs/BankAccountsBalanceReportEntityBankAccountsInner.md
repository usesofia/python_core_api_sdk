# BankAccountsBalanceReportEntityBankAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**bank_connection_id** | **str** |  | 
**bank_connection** | [**BankAccountEntityBankConnection**](BankAccountEntityBankConnection.md) |  | 
**provider** | **str** |  | 
**provider_account_id** | **str** |  | 
**type** | **str** |  | 
**enabled** | **bool** |  | 
**number** | **str** |  | 
**balance** | **int** |  | 
**currency_code** | **str** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.bank_accounts_balance_report_entity_bank_accounts_inner import BankAccountsBalanceReportEntityBankAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountsBalanceReportEntityBankAccountsInner from a JSON string
bank_accounts_balance_report_entity_bank_accounts_inner_instance = BankAccountsBalanceReportEntityBankAccountsInner.from_json(json)
# print the JSON string representation of the object
print(BankAccountsBalanceReportEntityBankAccountsInner.to_json())

# convert the object into a dict
bank_accounts_balance_report_entity_bank_accounts_inner_dict = bank_accounts_balance_report_entity_bank_accounts_inner_instance.to_dict()
# create an instance of BankAccountsBalanceReportEntityBankAccountsInner from a dict
bank_accounts_balance_report_entity_bank_accounts_inner_from_dict = BankAccountsBalanceReportEntityBankAccountsInner.from_dict(bank_accounts_balance_report_entity_bank_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


