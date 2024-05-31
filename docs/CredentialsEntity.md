# CredentialsEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.credentials_entity import CredentialsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsEntity from a JSON string
credentials_entity_instance = CredentialsEntity.from_json(json)
# print the JSON string representation of the object
print(CredentialsEntity.to_json())

# convert the object into a dict
credentials_entity_dict = credentials_entity_instance.to_dict()
# create an instance of CredentialsEntity from a dict
credentials_entity_from_dict = CredentialsEntity.from_dict(credentials_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


