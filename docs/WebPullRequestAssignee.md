# WebPullRequestAssignee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_assignee import WebPullRequestAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestAssignee from a JSON string
web_pull_request_assignee_instance = WebPullRequestAssignee.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestAssignee.to_json())

# convert the object into a dict
web_pull_request_assignee_dict = web_pull_request_assignee_instance.to_dict()
# create an instance of WebPullRequestAssignee from a dict
web_pull_request_assignee_from_dict = WebPullRequestAssignee.from_dict(web_pull_request_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


