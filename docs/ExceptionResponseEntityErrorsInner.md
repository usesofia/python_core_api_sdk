# ExceptionResponseEntityErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_path** | **str** |  | 
**messages** | **List[str]** |  | 

## Example

```python
from python_core_api_sdk.models.exception_response_entity_errors_inner import ExceptionResponseEntityErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionResponseEntityErrorsInner from a JSON string
exception_response_entity_errors_inner_instance = ExceptionResponseEntityErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ExceptionResponseEntityErrorsInner.to_json())

# convert the object into a dict
exception_response_entity_errors_inner_dict = exception_response_entity_errors_inner_instance.to_dict()
# create an instance of ExceptionResponseEntityErrorsInner from a dict
exception_response_entity_errors_inner_from_dict = ExceptionResponseEntityErrorsInner.from_dict(exception_response_entity_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


