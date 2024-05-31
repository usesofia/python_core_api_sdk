# ExceptionResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**message** | **str** |  | 
**errors** | [**List[ErrorEntity]**](ErrorEntity.md) |  | 

## Example

```python
from openapi_client.models.exception_response_entity import ExceptionResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionResponseEntity from a JSON string
exception_response_entity_instance = ExceptionResponseEntity.from_json(json)
# print the JSON string representation of the object
print(ExceptionResponseEntity.to_json())

# convert the object into a dict
exception_response_entity_dict = exception_response_entity_instance.to_dict()
# create an instance of ExceptionResponseEntity from a dict
exception_response_entity_from_dict = ExceptionResponseEntity.from_dict(exception_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


