# WebIssueActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**actor_access_role** | **str** |  | [optional] 
**actor_meta** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_activity import WebIssueActivity

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueActivity from a JSON string
web_issue_activity_instance = WebIssueActivity.from_json(json)
# print the JSON string representation of the object
print(WebIssueActivity.to_json())

# convert the object into a dict
web_issue_activity_dict = web_issue_activity_instance.to_dict()
# create an instance of WebIssueActivity from a dict
web_issue_activity_from_dict = WebIssueActivity.from_dict(web_issue_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


