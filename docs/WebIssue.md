# WebIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**comment_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**ended_at** | **str** |  | [optional] 
**labels** | [**List[LabelOption]**](LabelOption.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_reason** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue import WebIssue

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssue from a JSON string
web_issue_instance = WebIssue.from_json(json)
# print the JSON string representation of the object
print(WebIssue.to_json())

# convert the object into a dict
web_issue_dict = web_issue_instance.to_dict()
# create an instance of WebIssue from a dict
web_issue_from_dict = WebIssue.from_dict(web_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


