# EmailInUseReportEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**in_use** | **bool** |  | 

## Example

```python
from python_core_api_sdk.models.email_in_use_report_entity import EmailInUseReportEntity

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInUseReportEntity from a JSON string
email_in_use_report_entity_instance = EmailInUseReportEntity.from_json(json)
# print the JSON string representation of the object
print(EmailInUseReportEntity.to_json())

# convert the object into a dict
email_in_use_report_entity_dict = email_in_use_report_entity_instance.to_dict()
# create an instance of EmailInUseReportEntity from a dict
email_in_use_report_entity_from_dict = EmailInUseReportEntity.from_dict(email_in_use_report_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


