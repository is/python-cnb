# WebIssueType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_type import WebIssueType

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueType from a JSON string
web_issue_type_instance = WebIssueType.from_json(json)
# print the JSON string representation of the object
print(WebIssueType.to_json())

# convert the object into a dict
web_issue_type_dict = web_issue_type_instance.to_dict()
# create an instance of WebIssueType from a dict
web_issue_type_from_dict = WebIssueType.from_dict(web_issue_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


