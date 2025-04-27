# WebIssueTemplates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[WebIssueTemplate]**](WebIssueTemplate.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_templates import WebIssueTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueTemplates from a JSON string
web_issue_templates_instance = WebIssueTemplates.from_json(json)
# print the JSON string representation of the object
print(WebIssueTemplates.to_json())

# convert the object into a dict
web_issue_templates_dict = web_issue_templates_instance.to_dict()
# create an instance of WebIssueTemplates from a dict
web_issue_templates_from_dict = WebIssueTemplates.from_dict(web_issue_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


