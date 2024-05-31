# EmailInUseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**in_use** | **bool** |  | 

## Example

```python
from openapi_client.models.email_in_use_entity import EmailInUseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInUseEntity from a JSON string
email_in_use_entity_instance = EmailInUseEntity.from_json(json)
# print the JSON string representation of the object
print(EmailInUseEntity.to_json())

# convert the object into a dict
email_in_use_entity_dict = email_in_use_entity_instance.to_dict()
# create an instance of EmailInUseEntity from a dict
email_in_use_entity_from_dict = EmailInUseEntity.from_dict(email_in_use_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


