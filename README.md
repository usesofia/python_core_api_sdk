# python-core-api-sdk
Api principal do sistema Sofia.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.2
- Package version: 1.0.2
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import python_core_api_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import python_core_api_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import python_core_api_sdk
from python_core_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_core_api_sdk.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
async with python_core_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = python_core_api_sdk.BankAccountsApi(api_client)
    bank_account_id = 'bank_account_id_example' # str | 

    try:
        api_response = await api_instance.bank_accounts_controller_activate_bank_account(bank_account_id)
        print("The response of BankAccountsApi->bank_accounts_controller_activate_bank_account:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BankAccountsApi->bank_accounts_controller_activate_bank_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BankAccountsApi* | [**bank_accounts_controller_activate_bank_account**](docs/BankAccountsApi.md#bank_accounts_controller_activate_bank_account) | **POST** /bank/accounts/{bankAccountId}/activate | 
*BankAccountsApi* | [**bank_accounts_controller_create_or_update_bank_account**](docs/BankAccountsApi.md#bank_accounts_controller_create_or_update_bank_account) | **PUT** /workspaces/{workspaceId}/bank/accounts | 
*BankAccountsApi* | [**bank_accounts_controller_create_workspace_bank_accounts_balance_report**](docs/BankAccountsApi.md#bank_accounts_controller_create_workspace_bank_accounts_balance_report) | **POST** /workspaces/{workspaceId}/bank/accounts/balance-report | 
*BankAccountsApi* | [**bank_accounts_controller_disable_bank_account**](docs/BankAccountsApi.md#bank_accounts_controller_disable_bank_account) | **POST** /bank/accounts/{bankAccountId}/disable | 
*BankAccountsApi* | [**bank_accounts_controller_fetch_connection_bank_accounts**](docs/BankAccountsApi.md#bank_accounts_controller_fetch_connection_bank_accounts) | **GET** /workspaces/{workspaceId}/bank/connections/{bankConnectionId}/accounts | 
*BankAccountsApi* | [**bank_accounts_controller_fetch_workspace_bank_accounts**](docs/BankAccountsApi.md#bank_accounts_controller_fetch_workspace_bank_accounts) | **GET** /workspaces/{workspaceId}/bank/accounts | 
*BankAccountsApi* | [**bank_accounts_controller_get_bank_account_details**](docs/BankAccountsApi.md#bank_accounts_controller_get_bank_account_details) | **GET** /bank/accounts/{bankAccountId} | 
*BankConnectionsApi* | [**bank_connections_controller_activate_bank_connection**](docs/BankConnectionsApi.md#bank_connections_controller_activate_bank_connection) | **POST** /bank/connections/{bankConnectionId}/activate | 
*BankConnectionsApi* | [**bank_connections_controller_create_or_update_bank_connection**](docs/BankConnectionsApi.md#bank_connections_controller_create_or_update_bank_connection) | **PUT** /workspaces/{workspaceId}/bank/connections | 
*BankConnectionsApi* | [**bank_connections_controller_disable_bank_connection**](docs/BankConnectionsApi.md#bank_connections_controller_disable_bank_connection) | **POST** /bank/connections/{bankConnectionId}/disable | 
*BankConnectionsApi* | [**bank_connections_controller_fetch_user_bank_connections**](docs/BankConnectionsApi.md#bank_connections_controller_fetch_user_bank_connections) | **GET** /workspaces/{workspaceId}/bank/connections | 
*BankConnectionsApi* | [**bank_connections_controller_get_bank_connection_details**](docs/BankConnectionsApi.md#bank_connections_controller_get_bank_connection_details) | **GET** /bank/connections/{bankConnectionId} | 
*BankTransactionCategoriesApi* | [**bank_transaction_categories_controller_get_bank_transaction_categories**](docs/BankTransactionCategoriesApi.md#bank_transaction_categories_controller_get_bank_transaction_categories) | **GET** /workspaces/{workspaceId}/bank/transactions/categories | 
*BankTransactionTagsApi* | [**bank_transaction_tags_controller_create_tag**](docs/BankTransactionTagsApi.md#bank_transaction_tags_controller_create_tag) | **POST** /workspaces/{workspaceId}/bank/transactions/tags | 
*BankTransactionTagsApi* | [**bank_transaction_tags_controller_list_tags**](docs/BankTransactionTagsApi.md#bank_transaction_tags_controller_list_tags) | **GET** /workspaces/{workspaceId}/bank/transactions/tags | 
*BankTransactionsApi* | [**bank_transactions_controller_create_or_update_bank_transactions_in_bulk**](docs/BankTransactionsApi.md#bank_transactions_controller_create_or_update_bank_transactions_in_bulk) | **PUT** /bank/transactions/bulk | 
*BankTransactionsApi* | [**bank_transactions_controller_get_bank_transaction_by_provider**](docs/BankTransactionsApi.md#bank_transactions_controller_get_bank_transaction_by_provider) | **GET** /workspaces/{workspaceId}/bank/transactions/by-provider | 
*BankTransactionsApi* | [**bank_transactions_controller_get_bank_transactions**](docs/BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions) | **GET** /workspaces/{workspaceId}/bank/transactions | 
*BankTransactionsApi* | [**bank_transactions_controller_get_bank_transactions_confirmed_today_by_me**](docs/BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_confirmed_today_by_me) | **GET** /workspaces/{workspaceId}/bank/transactions/confirmed-today-by-me | 
*BankTransactionsApi* | [**bank_transactions_controller_get_bank_transactions_not_confirmed**](docs/BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_not_confirmed) | **GET** /workspaces/{workspaceId}/bank/transactions/not-confirmed | 
*BankTransactionsApi* | [**bank_transactions_controller_get_bank_transactions_totals**](docs/BankTransactionsApi.md#bank_transactions_controller_get_bank_transactions_totals) | **GET** /workspaces/{workspaceId}/bank/transactions/totals | 
*BankTransactionsApi* | [**bank_transactions_controller_get_recent**](docs/BankTransactionsApi.md#bank_transactions_controller_get_recent) | **GET** /workspaces/{workspaceId}/bank/transactions/most-recent | 
*BankTransactionsApi* | [**bank_transactions_controller_get_transaction_details**](docs/BankTransactionsApi.md#bank_transactions_controller_get_transaction_details) | **GET** /bank/transactions/{bankTransactionId} | 
*BankTransactionsApi* | [**bank_transactions_controller_update_transaction**](docs/BankTransactionsApi.md#bank_transactions_controller_update_transaction) | **PATCH** /bank/transactions/{bankTransactionId} | 
*IamAuthApi* | [**auth_controller_generate_and_send_email_verification_code**](docs/IamAuthApi.md#auth_controller_generate_and_send_email_verification_code) | **POST** /iam/auth/email-verification-code | 
*IamAuthApi* | [**auth_controller_generate_and_send_phone_verification_code**](docs/IamAuthApi.md#auth_controller_generate_and_send_phone_verification_code) | **POST** /iam/auth/phone-verification-code | 
*IamAuthApi* | [**auth_controller_refresh**](docs/IamAuthApi.md#auth_controller_refresh) | **POST** /iam/auth/refresh | 
*IamAuthApi* | [**auth_controller_sign_in_with_email**](docs/IamAuthApi.md#auth_controller_sign_in_with_email) | **POST** /iam/auth/sign-in/email | 
*IamAuthApi* | [**auth_controller_sign_up_with_email**](docs/IamAuthApi.md#auth_controller_sign_up_with_email) | **POST** /iam/auth/sign-up/email | 
*IamAuthApi* | [**auth_controller_verify_email_verification_code**](docs/IamAuthApi.md#auth_controller_verify_email_verification_code) | **GET** /iam/auth/email-verification-code/verify | 
*IamAuthApi* | [**auth_controller_verify_phone_verification_code**](docs/IamAuthApi.md#auth_controller_verify_phone_verification_code) | **GET** /iam/auth/phone-verification-code/verify | 
*MessageTokensApi* | [**message_tokens_controller_create_or_update_message_token**](docs/MessageTokensApi.md#message_tokens_controller_create_or_update_message_token) | **PUT** /workspaces/{workspaceId}/message-tokens | 
*MessageTokensApi* | [**message_tokens_controller_get_workspace_message_tokens**](docs/MessageTokensApi.md#message_tokens_controller_get_workspace_message_tokens) | **GET** /workspaces/{workspaceId}/message-tokens | 
*PluggyApi* | [**pluggy_controller_create**](docs/PluggyApi.md#pluggy_controller_create) | **POST** /pluggy/connect-token | 
*PluggyApi* | [**pluggy_controller_webhook**](docs/PluggyApi.md#pluggy_controller_webhook) | **POST** /pluggy/webhook | 
*ProfilesApi* | [**profiles_controller_create**](docs/ProfilesApi.md#profiles_controller_create) | **POST** /profiles | 
*ProfilesApi* | [**profiles_controller_get_my**](docs/ProfilesApi.md#profiles_controller_get_my) | **GET** /profiles/me | 
*ProfilesApi* | [**profiles_controller_parcial_update**](docs/ProfilesApi.md#profiles_controller_parcial_update) | **PATCH** /profiles/me | 
*ReportsApi* | [**reports_controller_get_accounts_entries_by_category_report**](docs/ReportsApi.md#reports_controller_get_accounts_entries_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/entries-by-category | 
*ReportsApi* | [**reports_controller_get_accounts_outputs_by_category_report**](docs/ReportsApi.md#reports_controller_get_accounts_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/outputs-by-category | 
*ReportsApi* | [**reports_controller_get_business_indicators**](docs/ReportsApi.md#reports_controller_get_business_indicators) | **GET** /workspaces/{workspaceId}/reports/indicators/business | 
*ReportsApi* | [**reports_controller_get_cards_cash_flow_report**](docs/ReportsApi.md#reports_controller_get_cards_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/cards/cash-flow | 
*ReportsApi* | [**reports_controller_get_cards_outputs_by_category_report**](docs/ReportsApi.md#reports_controller_get_cards_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/cards/outputs-by-category | 
*ReportsApi* | [**reports_controller_get_cash_flow_report**](docs/ReportsApi.md#reports_controller_get_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/accounts/cash-flow | 
*ReportsApi* | [**reports_controller_get_financial_statement_report**](docs/ReportsApi.md#reports_controller_get_financial_statement_report) | **GET** /workspaces/{workspaceId}/reports/financial-statement | 
*UsersApi* | [**users_controller_get**](docs/UsersApi.md#users_controller_get) | **GET** /users/users/{userId} | 
*WorkspaceJoinRequestsApi* | [**workspace_join_requests_controller_create_new_pending_or_return_current**](docs/WorkspaceJoinRequestsApi.md#workspace_join_requests_controller_create_new_pending_or_return_current) | **POST** /workspaces/{workspaceId}/join-requests | 
*WorkspacesApi* | [**workspaces_controller_create**](docs/WorkspacesApi.md#workspaces_controller_create) | **POST** /workspaces | 
*WorkspacesApi* | [**workspaces_controller_fetch_user_related_workspaces**](docs/WorkspacesApi.md#workspaces_controller_fetch_user_related_workspaces) | **GET** /workspaces/related-to-me | 
*WorkspacesApi* | [**workspaces_controller_get**](docs/WorkspacesApi.md#workspaces_controller_get) | **GET** /workspaces/{workspaceId} | 
*WorkspacesApi* | [**workspaces_controller_parcial_update**](docs/WorkspacesApi.md#workspaces_controller_parcial_update) | **PATCH** /workspaces/{workspaceId} | 


## Documentation For Models

 - [BalancePointResultEntity](docs/BalancePointResultEntity.md)
 - [BankAccountEntity](docs/BankAccountEntity.md)
 - [BankAccountsBalanceReportEntity](docs/BankAccountsBalanceReportEntity.md)
 - [BankAccountsBalanceReportItemEntity](docs/BankAccountsBalanceReportItemEntity.md)
 - [BankConnectionEntity](docs/BankConnectionEntity.md)
 - [BankConnectionWithAccountsEntity](docs/BankConnectionWithAccountsEntity.md)
 - [BankConnectorEntity](docs/BankConnectorEntity.md)
 - [BankTransactionCategoryEntity](docs/BankTransactionCategoryEntity.md)
 - [BankTransactionCategoryPlainEntity](docs/BankTransactionCategoryPlainEntity.md)
 - [BankTransactionCreditCardMetadataEntity](docs/BankTransactionCreditCardMetadataEntity.md)
 - [BankTransactionEntity](docs/BankTransactionEntity.md)
 - [BankTransactionIndicatorEntity](docs/BankTransactionIndicatorEntity.md)
 - [BankTransactionPaymentDataEntity](docs/BankTransactionPaymentDataEntity.md)
 - [BankTransactionTagEntity](docs/BankTransactionTagEntity.md)
 - [BankTransactionsPageEntity](docs/BankTransactionsPageEntity.md)
 - [BankTransactionsTotalsEntity](docs/BankTransactionsTotalsEntity.md)
 - [CashFlowByCategoryReportEntity](docs/CashFlowByCategoryReportEntity.md)
 - [CashFlowByCategoryReportItemEntity](docs/CashFlowByCategoryReportItemEntity.md)
 - [CashFlowReportDailyItemEntity](docs/CashFlowReportDailyItemEntity.md)
 - [CashFlowReportEntity](docs/CashFlowReportEntity.md)
 - [CashFlowReportMonthlyItemEntity](docs/CashFlowReportMonthlyItemEntity.md)
 - [CashFlowReportWeeklyItemEntity](docs/CashFlowReportWeeklyItemEntity.md)
 - [CategoryGuessDto](docs/CategoryGuessDto.md)
 - [CreateBankTransactionTagRequestDto](docs/CreateBankTransactionTagRequestDto.md)
 - [CreateOrUpdateBankAccountRequestDto](docs/CreateOrUpdateBankAccountRequestDto.md)
 - [CreateOrUpdateBankConnectionRequestDto](docs/CreateOrUpdateBankConnectionRequestDto.md)
 - [CreateOrUpdateBankTransactionsInBulkItemDto](docs/CreateOrUpdateBankTransactionsInBulkItemDto.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDto](docs/CreateOrUpdateBankTransactionsInBulkRequestDto.md)
 - [CreateOrUpdateMessageTokenRequestDto](docs/CreateOrUpdateMessageTokenRequestDto.md)
 - [CreatePluggyConnectTokenRequestDto](docs/CreatePluggyConnectTokenRequestDto.md)
 - [CreateProfileRequestDto](docs/CreateProfileRequestDto.md)
 - [CreateWorkspaceRequestDto](docs/CreateWorkspaceRequestDto.md)
 - [CredentialsEntity](docs/CredentialsEntity.md)
 - [CreditCardMetadataDto](docs/CreditCardMetadataDto.md)
 - [DreLineOutcomeResultEntity](docs/DreLineOutcomeResultEntity.md)
 - [ExceptionResponseEntity](docs/ExceptionResponseEntity.md)
 - [ExceptionResponseEntityErrorsInner](docs/ExceptionResponseEntityErrorsInner.md)
 - [FinancialStatementOutcomeReportDataEntity](docs/FinancialStatementOutcomeReportDataEntity.md)
 - [FinancialStatementOutflowsSubcategoryData](docs/FinancialStatementOutflowsSubcategoryData.md)
 - [FinancialStatementOutlfowsCategoryData](docs/FinancialStatementOutlfowsCategoryData.md)
 - [FinancialStatementReport](docs/FinancialStatementReport.md)
 - [FinancialStatementReportItemEntity](docs/FinancialStatementReportItemEntity.md)
 - [FinancialStatementeEntriesCategoryData](docs/FinancialStatementeEntriesCategoryData.md)
 - [FinancialStatementeEntriesSubcategoryData](docs/FinancialStatementeEntriesSubcategoryData.md)
 - [GenerateAndSendEmailVerificationCodeRequestDto](docs/GenerateAndSendEmailVerificationCodeRequestDto.md)
 - [GenerateAndSendPhoneVerificationCodeRequestDto](docs/GenerateAndSendPhoneVerificationCodeRequestDto.md)
 - [MeanResultEntity](docs/MeanResultEntity.md)
 - [MeanResultSubcategoryItemEntity](docs/MeanResultSubcategoryItemEntity.md)
 - [MessageTokenEntity](docs/MessageTokenEntity.md)
 - [ParcialUpdateProfileRequestDto](docs/ParcialUpdateProfileRequestDto.md)
 - [ParcialUpdateWorkspaceRequestDto](docs/ParcialUpdateWorkspaceRequestDto.md)
 - [PaymentDataDto](docs/PaymentDataDto.md)
 - [PlainBankAccountEntity](docs/PlainBankAccountEntity.md)
 - [PluggyConnectTokenEntity](docs/PluggyConnectTokenEntity.md)
 - [ProfileEntity](docs/ProfileEntity.md)
 - [ProportionResultEntity](docs/ProportionResultEntity.md)
 - [RefreshRequestDto](docs/RefreshRequestDto.md)
 - [SignInWithEmailRequestDto](docs/SignInWithEmailRequestDto.md)
 - [SignUpWithEmailRequestDto](docs/SignUpWithEmailRequestDto.md)
 - [UpdateBankTransactionRequestDto](docs/UpdateBankTransactionRequestDto.md)
 - [UserEntity](docs/UserEntity.md)
 - [UserRelatedWorkspaceEntity](docs/UserRelatedWorkspaceEntity.md)
 - [VerifyEmailVerificationCodeRequestDto](docs/VerifyEmailVerificationCodeRequestDto.md)
 - [VerifyPhoneVerificationCodeRequestDto](docs/VerifyPhoneVerificationCodeRequestDto.md)
 - [WorkspaceCompanySettingsEntity](docs/WorkspaceCompanySettingsEntity.md)
 - [WorkspaceEntity](docs/WorkspaceEntity.md)
 - [WorkspaceHybridSettingsEntity](docs/WorkspaceHybridSettingsEntity.md)
 - [WorkspaceJoinRequestEntity](docs/WorkspaceJoinRequestEntity.md)
 - [WorkspacePersonalSettingsEntity](docs/WorkspacePersonalSettingsEntity.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




