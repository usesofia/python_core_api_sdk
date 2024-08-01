# SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_provider_transaction_id** | **str** |  | 
**legal_nature** | [**SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature**](SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature.md) |  | 

## Example

```python
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner import SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner from a JSON string
sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_instance = SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.from_json(json)
# print the JSON string representation of the object
print(SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.to_json())

# convert the object into a dict
sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_dict = sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_instance.to_dict()
# create an instance of SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner from a dict
sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_from_dict = SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.from_dict(sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


