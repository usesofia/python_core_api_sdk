# AiChatFeatureSpecificationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**enabled** | **bool** |  | 
**subscription_product_id** | **str** |  | 

## Example

```python
from openapi_client.models.ai_chat_feature_specification_entity import AiChatFeatureSpecificationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatFeatureSpecificationEntity from a JSON string
ai_chat_feature_specification_entity_instance = AiChatFeatureSpecificationEntity.from_json(json)
# print the JSON string representation of the object
print(AiChatFeatureSpecificationEntity.to_json())

# convert the object into a dict
ai_chat_feature_specification_entity_dict = ai_chat_feature_specification_entity_instance.to_dict()
# create an instance of AiChatFeatureSpecificationEntity from a dict
ai_chat_feature_specification_entity_from_dict = AiChatFeatureSpecificationEntity.from_dict(ai_chat_feature_specification_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


