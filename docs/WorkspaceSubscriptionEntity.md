# WorkspaceSubscriptionEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**subscription_product_id** | **str** |  | 
**subscription_product** | [**SubscriptionProductEntity**](SubscriptionProductEntity.md) |  | 
**status** | **str** |  | 
**payment_system** | **str** |  | 
**payment_system_subscription_id** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.workspace_subscription_entity import WorkspaceSubscriptionEntity

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSubscriptionEntity from a JSON string
workspace_subscription_entity_instance = WorkspaceSubscriptionEntity.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSubscriptionEntity.to_json())

# convert the object into a dict
workspace_subscription_entity_dict = workspace_subscription_entity_instance.to_dict()
# create an instance of WorkspaceSubscriptionEntity from a dict
workspace_subscription_entity_from_dict = WorkspaceSubscriptionEntity.from_dict(workspace_subscription_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


