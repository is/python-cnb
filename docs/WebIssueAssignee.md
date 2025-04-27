# WebIssueAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_assignee import WebIssueAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueAssignee from a JSON string
web_issue_assignee_instance = WebIssueAssignee.from_json(json)
# print the JSON string representation of the object
print(WebIssueAssignee.to_json())

# convert the object into a dict
web_issue_assignee_dict = web_issue_assignee_instance.to_dict()
# create an instance of WebIssueAssignee from a dict
web_issue_assignee_from_dict = WebIssueAssignee.from_dict(web_issue_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


