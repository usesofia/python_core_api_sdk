# MessageTokenEntityWorksapce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pretty_id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**creator_user_id** | **str** |  | 
**selected_personal_category_tree_id** | **str** |  | [optional] 
**selected_business_category_tree_id** | **str** |  | [optional] 
**hybrid_settings** | [**UserEntityWorkspacesInnerHybridSettings**](UserEntityWorkspacesInnerHybridSettings.md) |  | [optional] 
**business_settings** | [**UserEntityWorkspacesInnerHybridSettings**](UserEntityWorkspacesInnerHybridSettings.md) |  | [optional] 
**personal_settings** | [**UserEntityWorkspacesInnerPersonalSettings**](UserEntityWorkspacesInnerPersonalSettings.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from python_core_api_sdk.models.message_token_entity_worksapce import MessageTokenEntityWorksapce

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTokenEntityWorksapce from a JSON string
message_token_entity_worksapce_instance = MessageTokenEntityWorksapce.from_json(json)
# print the JSON string representation of the object
print(MessageTokenEntityWorksapce.to_json())

# convert the object into a dict
message_token_entity_worksapce_dict = message_token_entity_worksapce_instance.to_dict()
# create an instance of MessageTokenEntityWorksapce from a dict
message_token_entity_worksapce_from_dict = MessageTokenEntityWorksapce.from_dict(message_token_entity_worksapce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


