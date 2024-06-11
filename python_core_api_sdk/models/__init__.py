# coding: utf-8

# flake8: noqa
"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from python_core_api_sdk.models.ai_chat_feature_specification_entity import AiChatFeatureSpecificationEntity
from python_core_api_sdk.models.balance_point_result_entity import BalancePointResultEntity
from python_core_api_sdk.models.bank_account_entity import BankAccountEntity
from python_core_api_sdk.models.bank_accounts_balance_report_entity import BankAccountsBalanceReportEntity
from python_core_api_sdk.models.bank_accounts_balance_report_item_entity import BankAccountsBalanceReportItemEntity
from python_core_api_sdk.models.bank_connection_entity import BankConnectionEntity
from python_core_api_sdk.models.bank_connection_with_accounts_entity import BankConnectionWithAccountsEntity
from python_core_api_sdk.models.bank_connector_entity import BankConnectorEntity
from python_core_api_sdk.models.bank_transaction_category_entity import BankTransactionCategoryEntity
from python_core_api_sdk.models.bank_transaction_category_plain_entity import BankTransactionCategoryPlainEntity
from python_core_api_sdk.models.bank_transaction_credit_card_metadata_entity import BankTransactionCreditCardMetadataEntity
from python_core_api_sdk.models.bank_transaction_entity import BankTransactionEntity
from python_core_api_sdk.models.bank_transaction_indicator_entity import BankTransactionIndicatorEntity
from python_core_api_sdk.models.bank_transaction_payment_data_entity import BankTransactionPaymentDataEntity
from python_core_api_sdk.models.bank_transaction_tag_entity import BankTransactionTagEntity
from python_core_api_sdk.models.bank_transactions_page_entity import BankTransactionsPageEntity
from python_core_api_sdk.models.cash_flow_by_category_report_entity import CashFlowByCategoryReportEntity
from python_core_api_sdk.models.cash_flow_by_category_report_item_entity import CashFlowByCategoryReportItemEntity
from python_core_api_sdk.models.cash_flow_report_daily_item_entity import CashFlowReportDailyItemEntity
from python_core_api_sdk.models.cash_flow_report_entity import CashFlowReportEntity
from python_core_api_sdk.models.cash_flow_report_monthly_item_entity import CashFlowReportMonthlyItemEntity
from python_core_api_sdk.models.cash_flow_report_weekly_item_entity import CashFlowReportWeeklyItemEntity
from python_core_api_sdk.models.category_guess_dto import CategoryGuessDto
from python_core_api_sdk.models.check_email_in_use_request_dto import CheckEmailInUseRequestDto
from python_core_api_sdk.models.checkout_session_entity import CheckoutSessionEntity
from python_core_api_sdk.models.connection_feature_specification_entity import ConnectionFeatureSpecificationEntity
from python_core_api_sdk.models.create_bank_transaction_tag_request_dto import CreateBankTransactionTagRequestDto
from python_core_api_sdk.models.create_or_update_bank_account_request_dto import CreateOrUpdateBankAccountRequestDto
from python_core_api_sdk.models.create_or_update_bank_connection_request_dto import CreateOrUpdateBankConnectionRequestDto
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_item_dto import CreateOrUpdateBankTransactionsInBulkItemDto
from python_core_api_sdk.models.create_or_update_bank_transactions_in_bulk_request_dto import CreateOrUpdateBankTransactionsInBulkRequestDto
from python_core_api_sdk.models.create_or_update_message_token_request_dto import CreateOrUpdateMessageTokenRequestDto
from python_core_api_sdk.models.create_pluggy_connect_token_request_dto import CreatePluggyConnectTokenRequestDto
from python_core_api_sdk.models.create_profile_request_dto import CreateProfileRequestDto
from python_core_api_sdk.models.create_stripe_checkout_session_request_dto import CreateStripeCheckoutSessionRequestDto
from python_core_api_sdk.models.create_workspace_request_dto import CreateWorkspaceRequestDto
from python_core_api_sdk.models.credentials_entity import CredentialsEntity
from python_core_api_sdk.models.credit_card_metadata_dto import CreditCardMetadataDto
from python_core_api_sdk.models.dre_line_outcome_result_entity import DreLineOutcomeResultEntity
from python_core_api_sdk.models.email_in_use_entity import EmailInUseEntity
from python_core_api_sdk.models.error_entity import ErrorEntity
from python_core_api_sdk.models.exception_response_entity import ExceptionResponseEntity
from python_core_api_sdk.models.financial_statement_outcome_report_data_entity import FinancialStatementOutcomeReportDataEntity
from python_core_api_sdk.models.financial_statement_outflows_subcategory_data import FinancialStatementOutflowsSubcategoryData
from python_core_api_sdk.models.financial_statement_outlfows_category_data import FinancialStatementOutlfowsCategoryData
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport
from python_core_api_sdk.models.financial_statement_report_item_entity import FinancialStatementReportItemEntity
from python_core_api_sdk.models.financial_statemente_entries_category_data import FinancialStatementeEntriesCategoryData
from python_core_api_sdk.models.financial_statemente_entries_subcategory_data import FinancialStatementeEntriesSubcategoryData
from python_core_api_sdk.models.financial_transactions_feature_specification_entity import FinancialTransactionsFeatureSpecificationEntity
from python_core_api_sdk.models.mean_result_entity import MeanResultEntity
from python_core_api_sdk.models.mean_result_subcategory_item_entity import MeanResultSubcategoryItemEntity
from python_core_api_sdk.models.message_token_entity import MessageTokenEntity
from python_core_api_sdk.models.parcial_update_profile_request_dto import ParcialUpdateProfileRequestDto
from python_core_api_sdk.models.parcial_update_workspace_request_dto import ParcialUpdateWorkspaceRequestDto
from python_core_api_sdk.models.payment_data_dto import PaymentDataDto
from python_core_api_sdk.models.payments_manager_product_data_entity import PaymentsManagerProductDataEntity
from python_core_api_sdk.models.payments_manager_product_price_entity import PaymentsManagerProductPriceEntity
from python_core_api_sdk.models.plain_bank_account_entity import PlainBankAccountEntity
from python_core_api_sdk.models.pluggy_connect_token_entity import PluggyConnectTokenEntity
from python_core_api_sdk.models.profile_entity import ProfileEntity
from python_core_api_sdk.models.proportion_result_entity import ProportionResultEntity
from python_core_api_sdk.models.refresh_request_dto import RefreshRequestDto
from python_core_api_sdk.models.send_email_verification_code_request_dto import SendEmailVerificationCodeRequestDto
from python_core_api_sdk.models.sign_in_with_email_password_request_dto import SignInWithEmailPasswordRequestDto
from python_core_api_sdk.models.sign_up_with_email_password_request_dto import SignUpWithEmailPasswordRequestDto
from python_core_api_sdk.models.subscription_product_entity import SubscriptionProductEntity
from python_core_api_sdk.models.update_bank_transaction_request_dto import UpdateBankTransactionRequestDto
from python_core_api_sdk.models.user_entity import UserEntity
from python_core_api_sdk.models.user_related_workspace_entity import UserRelatedWorkspaceEntity
from python_core_api_sdk.models.user_with_profile_entity import UserWithProfileEntity
from python_core_api_sdk.models.workspace_company_settings_entity import WorkspaceCompanySettingsEntity
from python_core_api_sdk.models.workspace_entity import WorkspaceEntity
from python_core_api_sdk.models.workspace_hybrid_settings_entity import WorkspaceHybridSettingsEntity
from python_core_api_sdk.models.workspace_join_request_entity import WorkspaceJoinRequestEntity
from python_core_api_sdk.models.workspace_personal_settings_entity import WorkspacePersonalSettingsEntity
from python_core_api_sdk.models.workspace_subscription_entity import WorkspaceSubscriptionEntity
