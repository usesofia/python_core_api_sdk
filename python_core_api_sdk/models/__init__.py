# coding: utf-8

# flake8: noqa
"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from python_core_api_sdk.models.assign_category_for_bank_transactions_page_request_dto import AssignCategoryForBankTransactionsPageRequestDto
from python_core_api_sdk.models.assign_legal_nature_for_bank_transactions_page_request_dto import AssignLegalNatureForBankTransactionsPageRequestDto
from python_core_api_sdk.models.balance_point_result_entity import BalancePointResultEntity
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity
from python_core_api_sdk.models.bank_accounts_balance_report_entity_items_inner import BankAccountsBalanceReportEntityItemsInner
from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
from python_core_api_sdk.models.bank_connection_entity_accounts_inner import BankConnectionEntityAccountsInner
from python_core_api_sdk.models.bank_connection_entity_connector import BankConnectionEntityConnector
from python_core_api_sdk.models.bank_transaction_category_entity import BankTransactionCategoryEntity
from python_core_api_sdk.models.bank_transaction_category_entity_children_inner import BankTransactionCategoryEntityChildrenInner
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.bank_transaction_entity_account import BankTransactionEntityAccount
from python_core_api_sdk.models.bank_transaction_entity_account_bank_connection import BankTransactionEntityAccountBankConnection
from python_core_api_sdk.models.bank_transaction_entity_category import BankTransactionEntityCategory
from python_core_api_sdk.models.bank_transaction_entity_credit_card_metadata import BankTransactionEntityCreditCardMetadata
from python_core_api_sdk.models.bank_transaction_entity_payment_data import BankTransactionEntityPaymentData
from python_core_api_sdk.models.bank_transaction_entity_tags_inner import BankTransactionEntityTagsInner
from python_core_api_sdk.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity
from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
from python_core_api_sdk.models.bank_transactions_page_entity_items_inner import BankTransactionsPageEntityItemsInner
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.models.cash_flow_by_category_report_item_entity import CashFlowByCategoryReportItemEntity
from python_core_api_sdk.models.cash_flow_report_daily_item_entity import CashFlowReportDailyItemEntity
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.models.cash_flow_report_monthly_item_entity import CashFlowReportMonthlyItemEntity
from python_core_api_sdk.models.cash_flow_report_weekly_item_entity import CashFlowReportWeeklyItemEntity
from python_core_api_sdk.models.create_bank_transaction_tag_request_dto import CreateBankTransactionTagRequestDto
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInner
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_category_guesses_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCategoryGuessesInner
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_credit_card_metadata import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerCreditCardMetadata
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_legal_nature_guesses_inner import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerLegalNatureGuessesInner
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto_items_inner_payment_data import CreateOrUpdateBankTransactionsInBulkRequestDtoItemsInnerPaymentData
from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto
from python_core_api_sdk.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto
from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.dre_line_outcome_result_entity import DreLineOutcomeResultEntity
from python_core_api_sdk.models.email_in_use_report_entity import EmailInUseReportEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.exception_response_entity_errors_inner import ExceptionResponseEntityErrorsInner
from python_core_api_sdk.models.financial_statement_outcome_report_data_entity import FinancialStatementOutcomeReportDataEntity
from python_core_api_sdk.models.financial_statement_outflows_subcategory_data import FinancialStatementOutflowsSubcategoryData
from python_core_api_sdk.models.financial_statement_outlfows_category_data import FinancialStatementOutlfowsCategoryData
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport
from python_core_api_sdk.models.financial_statement_report_item_entity import FinancialStatementReportItemEntity
from python_core_api_sdk.models.financial_statemente_entries_category_data import FinancialStatementeEntriesCategoryData
from python_core_api_sdk.models.financial_statemente_entries_subcategory_data import FinancialStatementeEntriesSubcategoryData
from python_core_api_sdk.models.generate_and_send_email_verification_code_request_dto import GenerateAndSendEmailVerificationCodeRequestDto
from python_core_api_sdk.models.generate_and_send_phone_verification_code_request_dto import GenerateAndSendPhoneVerificationCodeRequestDto
from python_core_api_sdk.models.generate_email_in_use_report_request_dto import GenerateEmailInUseReportRequestDto
from python_core_api_sdk.models.generate_phone_in_use_report_request_dto import GeneratePhoneInUseReportRequestDto
from python_core_api_sdk.models.mean_result_entity import MeanResultEntity
from python_core_api_sdk.models.mean_result_subcategory_item_entity import MeanResultSubcategoryItemEntity
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity
from python_core_api_sdk.models.message_token_entity_user import MessageTokenEntityUser
from python_core_api_sdk.models.message_token_entity_worksapce import MessageTokenEntityWorksapce
from python_core_api_sdk.models.partial_update_bank_transaction_request_dto import PartialUpdateBankTransactionRequestDto
from python_core_api_sdk.models.partial_update_profile_request_dto import PartialUpdateProfileRequestDto
from python_core_api_sdk.models.partial_update_workspace_request_dto import PartialUpdateWorkspaceRequestDto
from python_core_api_sdk.models.pluggy_connect_token_entity import PluggyConnectTokenEntity
from python_core_api_sdk.models.profile_entity import ProfileEntity
from python_core_api_sdk.models.proportion_result_entity import ProportionResultEntity
from python_core_api_sdk.models.refresh_request_dto import RefreshRequestDto
from python_core_api_sdk.models.sign_in_with_email_request_dto import SignInWithEmailRequestDto
from python_core_api_sdk.models.sign_up_with_email_request_dto import SignUpWithEmailRequestDto
from python_core_api_sdk.models.sync_bank_account_transactions_page_begin_request_dto import SyncBankAccountTransactionsPageBeginRequestDto
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto import SyncBankAccountTransactionsPageEndRequestDto
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPage
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInner
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_credit_card_metadata import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerCreditCardMetadata
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_bank_provider_transactions_page_transactions_inner_payment_data import SyncBankAccountTransactionsPageEndRequestDtoBankProviderTransactionsPageTransactionsInnerPaymentData
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_category_assign_requests_inner import SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInner
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_category_assign_requests_inner_category import SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategory
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_category_assign_requests_inner_category_prediction_response import SyncBankAccountTransactionsPageEndRequestDtoCategoryAssignRequestsInnerCategoryPredictionResponse
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner import SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInner
from python_core_api_sdk.models.sync_bank_account_transactions_page_end_request_dto_legal_nature_assign_requests_inner_legal_nature import SyncBankAccountTransactionsPageEndRequestDtoLegalNatureAssignRequestsInnerLegalNature
from python_core_api_sdk.models.sync_bank_account_transactions_request_dto import SyncBankAccountTransactionsRequestDto
from python_core_api_sdk.models.sync_bank_item_request_dto import SyncBankItemRequestDto
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk.models.user_entity_workspaces_inner import UserEntityWorkspacesInner
from python_core_api_sdk.models.user_entity_workspaces_inner_hybrid_settings import UserEntityWorkspacesInnerHybridSettings
from python_core_api_sdk.models.user_entity_workspaces_inner_personal_settings import UserEntityWorkspacesInnerPersonalSettings
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity
from python_core_api_sdk.models.verify_email_verification_code_request_dto import VerifyEmailVerificationCodeRequestDto
from python_core_api_sdk.models.verify_phone_verification_code_request_dto import VerifyPhoneVerificationCodeRequestDto
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
