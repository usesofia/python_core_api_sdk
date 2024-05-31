# FinancialStatementReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FinancialStatementReportItemEntity]**](FinancialStatementReportItemEntity.md) |  | 

## Example

```python
from python_core_api_sdk.models.financial_statement_report import FinancialStatementReport

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialStatementReport from a JSON string
financial_statement_report_instance = FinancialStatementReport.from_json(json)
# print the JSON string representation of the object
print(FinancialStatementReport.to_json())

# convert the object into a dict
financial_statement_report_dict = financial_statement_report_instance.to_dict()
# create an instance of FinancialStatementReport from a dict
financial_statement_report_from_dict = FinancialStatementReport.from_dict(financial_statement_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


