# SubscriptionProductEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**payment_system** | **str** |  | 
**payment_system_product_id** | **str** |  | 
**workspace_type** | **str** |  | 
**trial_period_in_days** | **float** |  | [optional] 
**trial_already_used** | **bool** |  | [optional] 
**connection_feature_specification** | [**ConnectionFeatureSpecificationEntity**](ConnectionFeatureSpecificationEntity.md) |  | 
**financial_transactions_feature_specification** | [**FinancialTransactionsFeatureSpecificationEntity**](FinancialTransactionsFeatureSpecificationEntity.md) |  | 
**ai_chat_feature_specification** | [**AiChatFeatureSpecificationEntity**](AiChatFeatureSpecificationEntity.md) |  | 
**payments_manager_data** | [**PaymentsManagerProductDataEntity**](PaymentsManagerProductDataEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.subscription_product_entity import SubscriptionProductEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionProductEntity from a JSON string
subscription_product_entity_instance = SubscriptionProductEntity.from_json(json)
# print the JSON string representation of the object
print(SubscriptionProductEntity.to_json())

# convert the object into a dict
subscription_product_entity_dict = subscription_product_entity_instance.to_dict()
# create an instance of SubscriptionProductEntity from a dict
subscription_product_entity_from_dict = SubscriptionProductEntity.from_dict(subscription_product_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


