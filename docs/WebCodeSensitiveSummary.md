# WebCodeSensitiveSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignored** | **int** | 忽略问题数量 | [optional] 
**open** | **int** | 开启中问题数量 | [optional] 

## Example

```python
from cnb_api.models.web_code_sensitive_summary import WebCodeSensitiveSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WebCodeSensitiveSummary from a JSON string
web_code_sensitive_summary_instance = WebCodeSensitiveSummary.from_json(json)
# print the JSON string representation of the object
print(WebCodeSensitiveSummary.to_json())

# convert the object into a dict
web_code_sensitive_summary_dict = web_code_sensitive_summary_instance.to_dict()
# create an instance of WebCodeSensitiveSummary from a dict
web_code_sensitive_summary_from_dict = WebCodeSensitiveSummary.from_dict(web_code_sensitive_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


