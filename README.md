# python-core-api-sdk
Api principal do sistema Sofia.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.5
- Package version: 1.0.5
- Generator version: 7.7.0
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
    api_instance = python_core_api_sdk.AuthApi(api_client)
    generate_and_send_email_verification_code_request_dto = python_core_api_sdk.GenerateAndSendEmailVerificationCodeRequestDto() # GenerateAndSendEmailVerificationCodeRequestDto | 

    try:
        await api_instance.auth_controller_generate_and_send_email_verification_code(generate_and_send_email_verification_code_request_dto)
    except ApiException as e:
        print("Exception when calling AuthApi->auth_controller_generate_and_send_email_verification_code: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_controller_generate_and_send_email_verification_code**](docs/AuthApi.md#auth_controller_generate_and_send_email_verification_code) | **POST** /iam/auth/email-verification-code | 
*AuthApi* | [**auth_controller_generate_and_send_phone_verification_code**](docs/AuthApi.md#auth_controller_generate_and_send_phone_verification_code) | **POST** /iam/auth/phone-verification-code | 
*AuthApi* | [**auth_controller_generate_email_in_use_report**](docs/AuthApi.md#auth_controller_generate_email_in_use_report) | **POST** /iam/auth/email-in-use | 
*AuthApi* | [**auth_controller_generate_phone_in_use_report**](docs/AuthApi.md#auth_controller_generate_phone_in_use_report) | **POST** /iam/auth/phone-in-use | 
*AuthApi* | [**auth_controller_get_me**](docs/AuthApi.md#auth_controller_get_me) | **GET** /iam/auth/me | 
*AuthApi* | [**auth_controller_refresh**](docs/AuthApi.md#auth_controller_refresh) | **POST** /iam/auth/refresh | 
*AuthApi* | [**auth_controller_sign_in_with_email**](docs/AuthApi.md#auth_controller_sign_in_with_email) | **POST** /iam/auth/sign-in/email | 
*AuthApi* | [**auth_controller_sign_up_with_email**](docs/AuthApi.md#auth_controller_sign_up_with_email) | **POST** /iam/auth/sign-up/email | 
*AuthApi* | [**auth_controller_verify_email_verification_code**](docs/AuthApi.md#auth_controller_verify_email_verification_code) | **GET** /iam/auth/email-verification-code/verify | 
*AuthApi* | [**auth_controller_verify_phone_verification_code**](docs/AuthApi.md#auth_controller_verify_phone_verification_code) | **GET** /iam/auth/phone-verification-code/verify | 
*BankAccountsApi* | [**bank_accounts_controller_activate**](docs/BankAccountsApi.md#bank_accounts_controller_activate) | **POST** /bank/accounts/{bankAccountId}/activate | 
*BankAccountsApi* | [**bank_accounts_controller_create_or_update**](docs/BankAccountsApi.md#bank_accounts_controller_create_or_update) | **PUT** /bank/accounts | 
*BankAccountsApi* | [**bank_accounts_controller_disable**](docs/BankAccountsApi.md#bank_accounts_controller_disable) | **POST** /bank/accounts/{bankAccountId}/disable | 
*BankAccountsApi* | [**bank_accounts_controller_get_by_id**](docs/BankAccountsApi.md#bank_accounts_controller_get_by_id) | **GET** /bank/accounts/{bankAccountId} | 
*BankAccountsApi* | [**bank_accounts_controller_list_by_bank_connection_id**](docs/BankAccountsApi.md#bank_accounts_controller_list_by_bank_connection_id) | **GET** /bank/connections/{bankConnectionId}/accounts | 
*BankAccountsApi* | [**bank_accounts_controller_list_by_workspace_id**](docs/BankAccountsApi.md#bank_accounts_controller_list_by_workspace_id) | **GET** /bank/workspaces/{workspaceId}/accounts | 
*BankConnectionsApi* | [**bank_connections_controller_activate**](docs/BankConnectionsApi.md#bank_connections_controller_activate) | **POST** /bank/connections/{bankConnectionId}/activate | 
*BankConnectionsApi* | [**bank_connections_controller_create_or_update**](docs/BankConnectionsApi.md#bank_connections_controller_create_or_update) | **PUT** /bank/workspaces/{workspaceId}/connections | 
*BankConnectionsApi* | [**bank_connections_controller_disable**](docs/BankConnectionsApi.md#bank_connections_controller_disable) | **POST** /bank/connections/{bankConnectionId}/disable | 
*BankConnectionsApi* | [**bank_connections_controller_get_by_id**](docs/BankConnectionsApi.md#bank_connections_controller_get_by_id) | **GET** /bank/connections/{bankConnectionId} | 
*BankConnectionsApi* | [**bank_connections_controller_list**](docs/BankConnectionsApi.md#bank_connections_controller_list) | **GET** /bank/workspaces/{workspaceId}/connections | 
*BankSyncApi* | [**bank_sync_controller_sync_account_transactions**](docs/BankSyncApi.md#bank_sync_controller_sync_account_transactions) | **POST** /bank/sync/transactions | 
*BankSyncApi* | [**bank_sync_controller_sync_item**](docs/BankSyncApi.md#bank_sync_controller_sync_item) | **POST** /bank/sync/items | 
*BankSyncApi* | [**bank_sync_controller_sync_transactions_page_begin**](docs/BankSyncApi.md#bank_sync_controller_sync_transactions_page_begin) | **POST** /bank/sync/transactions/page/begin | 
*BankSyncApi* | [**bank_sync_controller_sync_transactions_page_end**](docs/BankSyncApi.md#bank_sync_controller_sync_transactions_page_end) | **POST** /bank/sync/transactions/page/end | 
*BankTransactionCategoriesApi* | [**bank_transaction_categories_controller_list**](docs/BankTransactionCategoriesApi.md#bank_transaction_categories_controller_list) | **GET** /bank/workspaces/{workspaceId}/transaction-categories | 
*BankTransactionTagsApi* | [**bank_transaction_tags_controller_create**](docs/BankTransactionTagsApi.md#bank_transaction_tags_controller_create) | **POST** /bank/workspaces/{workspaceId}/transaction-tags | 
*BankTransactionTagsApi* | [**bank_transaction_tags_controller_list**](docs/BankTransactionTagsApi.md#bank_transaction_tags_controller_list) | **GET** /bank/workspaces/{workspaceId}/transaction-tags | 
*BankTransactionsApi* | [**bank_transactions_controller_create_or_update_in_bulk**](docs/BankTransactionsApi.md#bank_transactions_controller_create_or_update_in_bulk) | **PUT** /bank/transactions/bulk | 
*BankTransactionsApi* | [**bank_transactions_controller_get_by_id**](docs/BankTransactionsApi.md#bank_transactions_controller_get_by_id) | **GET** /bank/transactions/{bankTransactionId} | 
*BankTransactionsApi* | [**bank_transactions_controller_get_by_provider**](docs/BankTransactionsApi.md#bank_transactions_controller_get_by_provider) | **GET** /bank/accounts/{accountId}/transactions/by-provider | 
*BankTransactionsApi* | [**bank_transactions_controller_get_totals**](docs/BankTransactionsApi.md#bank_transactions_controller_get_totals) | **GET** /bank/workspaces/{workspaceId}/transactions/totals | 
*BankTransactionsApi* | [**bank_transactions_controller_list**](docs/BankTransactionsApi.md#bank_transactions_controller_list) | **GET** /bank/workspaces/{workspaceId}/transactions | 
*BankTransactionsApi* | [**bank_transactions_controller_list_most_recent**](docs/BankTransactionsApi.md#bank_transactions_controller_list_most_recent) | **GET** /bank/workspaces/{workspaceId}/transactions/most-recent | 
*BankTransactionsApi* | [**bank_transactions_controller_list_not_verified**](docs/BankTransactionsApi.md#bank_transactions_controller_list_not_verified) | **GET** /bank/workspaces/{workspaceId}/transactions/not-verified | 
*BankTransactionsApi* | [**bank_transactions_controller_list_verified_by_me**](docs/BankTransactionsApi.md#bank_transactions_controller_list_verified_by_me) | **GET** /bank/workspaces/{workspaceId}/transactions/verified-by-me | 
*BankTransactionsApi* | [**bank_transactions_controller_partial_update**](docs/BankTransactionsApi.md#bank_transactions_controller_partial_update) | **PATCH** /bank/transactions/{bankTransactionId} | 
*BankTransactionsPageCategoryAssignerApi* | [**bank_transactions_page_category_assigner_controller_assign**](docs/BankTransactionsPageCategoryAssignerApi.md#bank_transactions_page_category_assigner_controller_assign) | **POST** /bank/transactions/page/category/assign | 
*BankTransactionsPageLegalNatureAssignerApi* | [**bank_transactions_page_legal_nature_assigner_controller_assign**](docs/BankTransactionsPageLegalNatureAssignerApi.md#bank_transactions_page_legal_nature_assigner_controller_assign) | **POST** /bank/transactions/page/legal-nature/assign | 
*HelloApi* | [**hello_controller_hello**](docs/HelloApi.md#hello_controller_hello) | **GET** /hello | 
*MessageTokensApi* | [**message_tokens_controller_create_or_update**](docs/MessageTokensApi.md#message_tokens_controller_create_or_update) | **PUT** /communication/workspaces/{workspaceId}/message-tokens | 
*MessageTokensApi* | [**message_tokens_controller_list_by_workspace_id**](docs/MessageTokensApi.md#message_tokens_controller_list_by_workspace_id) | **GET** /communication/workspaces/{workspaceId}/message-tokens | 
*PluggyApi* | [**pluggy_controller_create_connect_token**](docs/PluggyApi.md#pluggy_controller_create_connect_token) | **POST** /pluggy/connect-tokens | 
*PluggyApi* | [**pluggy_controller_webhook**](docs/PluggyApi.md#pluggy_controller_webhook) | **POST** /pluggy/webhook | 
*ProfilesApi* | [**profiles_controller_create**](docs/ProfilesApi.md#profiles_controller_create) | **POST** /iam/profiles | 
*ProfilesApi* | [**profiles_controller_get_my**](docs/ProfilesApi.md#profiles_controller_get_my) | **GET** /iam/profiles/me | 
*ProfilesApi* | [**profiles_controller_partial_update**](docs/ProfilesApi.md#profiles_controller_partial_update) | **PATCH** /iam/profiles/me | 
*ReportsApi* | [**reports_controller_get_accounts_entries_by_category_report**](docs/ReportsApi.md#reports_controller_get_accounts_entries_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/entries-by-category | 
*ReportsApi* | [**reports_controller_get_accounts_outputs_by_category_report**](docs/ReportsApi.md#reports_controller_get_accounts_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/accounts/outputs-by-category | 
*ReportsApi* | [**reports_controller_get_business_indicators**](docs/ReportsApi.md#reports_controller_get_business_indicators) | **GET** /workspaces/{workspaceId}/reports/indicators/business | 
*ReportsApi* | [**reports_controller_get_cards_cash_flow_report**](docs/ReportsApi.md#reports_controller_get_cards_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/cards/cash-flow | 
*ReportsApi* | [**reports_controller_get_cards_outputs_by_category_report**](docs/ReportsApi.md#reports_controller_get_cards_outputs_by_category_report) | **GET** /workspaces/{workspaceId}/reports/cards/outputs-by-category | 
*ReportsApi* | [**reports_controller_get_cash_flow_report**](docs/ReportsApi.md#reports_controller_get_cash_flow_report) | **GET** /workspaces/{workspaceId}/reports/accounts/cash-flow | 
*ReportsApi* | [**reports_controller_get_financial_statement_report**](docs/ReportsApi.md#reports_controller_get_financial_statement_report) | **GET** /workspaces/{workspaceId}/reports/financial-statement | 
*WorkspacesApi* | [**workspaces_controller_create**](docs/WorkspacesApi.md#workspaces_controller_create) | **POST** /iam/workspaces | 
*WorkspacesApi* | [**workspaces_controller_get_by_id**](docs/WorkspacesApi.md#workspaces_controller_get_by_id) | **GET** /iam/workspaces/{workspaceId} | 
*WorkspacesApi* | [**workspaces_controller_list_my**](docs/WorkspacesApi.md#workspaces_controller_list_my) | **GET** /iam/workspaces/my | 
*WorkspacesApi* | [**workspaces_controller_partial_update**](docs/WorkspacesApi.md#workspaces_controller_partial_update) | **PATCH** /iam/workspaces/{workspaceId} | 


## Documentation For Models

 - [AssignCategoryForBankTransactionsPageRequestDto](docs/AssignCategoryForBankTransactionsPageRequestDto.md)
 - [AssignLegalNatureForBankTransactionsPageRequestDto](docs/AssignLegalNatureForBankTransactionsPageRequestDto.md)
 - [BalancePointResultEntity](docs/BalancePointResultEntity.md)
 - [BankAccountEntity](docs/BankAccountEntity.md)
 - [BankConnectionEntity](docs/BankConnectionEntity.md)
 - [BankConnectionEntityAccountsInner](docs/BankConnectionEntityAccountsInner.md)
 - [BankConnectionEntityConnector](docs/BankConnectionEntityConnector.md)
 - [BankTransactionCategoryEntity](docs/BankTransactionCategoryEntity.md)
 - [BankTransactionCategoryEntityChildrenInner](docs/BankTransactionCategoryEntityChildrenInner.md)
 - [BankTransactionEntity](docs/BankTransactionEntity.md)
 - [BankTransactionEntityCategory](docs/BankTransactionEntityCategory.md)
 - [BankTransactionEntityCreditCardMetadata](docs/BankTransactionEntityCreditCardMetadata.md)
 - [BankTransactionEntityPaymentData](docs/BankTransactionEntityPaymentData.md)
 - [BankTransactionEntityTagsInner](docs/BankTransactionEntityTagsInner.md)
 - [BankTransactionIndicatorEntity](docs/BankTransactionIndicatorEntity.md)
 - [BankTransactionTagEntity](docs/BankTransactionTagEntity.md)
 - [BankTransactionsPageEntity](docs/BankTransactionsPageEntity.md)
 - [BankTransactionsPageEntityItemsInner](docs/BankTransactionsPageEntityItemsInner.md)
 - [CashFlowByCategoryReportEntity](docs/CashFlowByCategoryReportEntity.md)
 - [CashFlowByCategoryReportItemEntity](docs/CashFlowByCategoryReportItemEntity.md)
 - [CashFlowReportDailyItemEntity](docs/CashFlowReportDailyItemEntity.md)
 - [CashFlowReportEntity](docs/CashFlowReportEntity.md)
 - [CashFlowReportMonthlyItemEntity](docs/CashFlowReportMonthlyItemEntity.md)
 - [CashFlowReportWeeklyItemEntity](docs/CashFlowReportWeeklyItemEntity.md)
 - [CreateBankTransactionTagRequestDto](docs/CreateBankTransactionTagRequestDto.md)
 - [CreateOrUpdateBankAccountRequestDto](docs/CreateOrUpdateBankAccountRequestDto.md)
 - [CreateOrUpdateBankConnectionRequestDto](docs/CreateOrUpdateBankConnectionRequestDto.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDto](docs/CreateOrUpdateBankTransactionsInBulkRequestDto.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner](docs/CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner](docs/CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata](docs/CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner](docs/CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner.md)
 - [CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData](docs/CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData.md)
 - [CreateOrUpdateMessageTokenRequestDto](docs/CreateOrUpdateMessageTokenRequestDto.md)
 - [CreatePluggyConnectTokenRequestDto](docs/CreatePluggyConnectTokenRequestDto.md)
 - [CreateProfileRequestDto](docs/CreateProfileRequestDto.md)
 - [CreateWorkspaceRequestDto](docs/CreateWorkspaceRequestDto.md)
 - [CredentialsEntity](docs/CredentialsEntity.md)
 - [DreLineOutcomeResultEntity](docs/DreLineOutcomeResultEntity.md)
 - [EmailInUseReportEntity](docs/EmailInUseReportEntity.md)
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
 - [GenerateEmailInUseReportRequestDto](docs/GenerateEmailInUseReportRequestDto.md)
 - [GeneratePhoneInUseReportRequestDto](docs/GeneratePhoneInUseReportRequestDto.md)
 - [MeanResultEntity](docs/MeanResultEntity.md)
 - [MeanResultSubcategoryItemEntity](docs/MeanResultSubcategoryItemEntity.md)
 - [MessageTokenEntity](docs/MessageTokenEntity.md)
 - [MessageTokenEntityUser](docs/MessageTokenEntityUser.md)
 - [MessageTokenEntityWorksapce](docs/MessageTokenEntityWorksapce.md)
 - [PartialUpdateBankTransactionRequestDto](docs/PartialUpdateBankTransactionRequestDto.md)
 - [PartialUpdateProfileRequestDto](docs/PartialUpdateProfileRequestDto.md)
 - [PartialUpdateWorkspaceRequestDto](docs/PartialUpdateWorkspaceRequestDto.md)
 - [PluggyConnectTokenEntity](docs/PluggyConnectTokenEntity.md)
 - [ProfileEntity](docs/ProfileEntity.md)
 - [ProportionResultEntity](docs/ProportionResultEntity.md)
 - [RefreshRequestDto](docs/RefreshRequestDto.md)
 - [SignInWithEmailRequestDto](docs/SignInWithEmailRequestDto.md)
 - [SignUpWithEmailRequestDto](docs/SignUpWithEmailRequestDto.md)
 - [SyncBankAccountTransactionsPageBeginRequestDto](docs/SyncBankAccountTransactionsPageBeginRequestDto.md)
 - [SyncBankAccountTransactionsPageEndRequestDto](docs/SyncBankAccountTransactionsPageEndRequestDto.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage](docs/SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner](docs/SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata](docs/SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData](docs/SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInner](docs/SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInner.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategory](docs/SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategory.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategoryPredictionResponse](docs/SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategoryPredictionResponse.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner](docs/SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner.md)
 - [SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature](docs/SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature.md)
 - [SyncBankAccountTransactionsRequestDto](docs/SyncBankAccountTransactionsRequestDto.md)
 - [SyncBankItemRequestDto](docs/SyncBankItemRequestDto.md)
 - [UserEntity](docs/UserEntity.md)
 - [UserEntityWorkspacesInner](docs/UserEntityWorkspacesInner.md)
 - [UserEntityWorkspacesInnerHybridSettings](docs/UserEntityWorkspacesInnerHybridSettings.md)
 - [UserEntityWorkspacesInnerPersonalSettings](docs/UserEntityWorkspacesInnerPersonalSettings.md)
 - [UserRelatedWorkspaceEntity](docs/UserRelatedWorkspaceEntity.md)
 - [VerifyEmailVerificationCodeRequestDto](docs/VerifyEmailVerificationCodeRequestDto.md)
 - [VerifyPhoneVerificationCodeRequestDto](docs/VerifyPhoneVerificationCodeRequestDto.md)
 - [WorkspaceEntity](docs/WorkspaceEntity.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




