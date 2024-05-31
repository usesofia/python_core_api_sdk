# CategoryGuessDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | 
**name** | **str** |  | 
**score** | **float** |  | 
**origin** | **str** |  | 

## Example

```python
from python_core_api_sdk.models.category_guess_dto import CategoryGuessDto

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryGuessDto from a JSON string
category_guess_dto_instance = CategoryGuessDto.from_json(json)
# print the JSON string representation of the object
print(CategoryGuessDto.to_json())

# convert the object into a dict
category_guess_dto_dict = category_guess_dto_instance.to_dict()
# create an instance of CategoryGuessDto from a dict
category_guess_dto_from_dict = CategoryGuessDto.from_dict(category_guess_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


