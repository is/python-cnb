# WebIssueTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_template import WebIssueTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueTemplate from a JSON string
web_issue_template_instance = WebIssueTemplate.from_json(json)
# print the JSON string representation of the object
print(WebIssueTemplate.to_json())

# convert the object into a dict
web_issue_template_dict = web_issue_template_instance.to_dict()
# create an instance of WebIssueTemplate from a dict
web_issue_template_from_dict = WebIssueTemplate.from_dict(web_issue_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


