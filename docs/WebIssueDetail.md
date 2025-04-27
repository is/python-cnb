# WebIssueDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[WebIssueAssignee]**](WebIssueAssignee.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**ended_at** | **str** |  | [optional] 
**labels** | [**List[LabelOption]**](LabelOption.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**participants** | [**List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_reason** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_detail import WebIssueDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueDetail from a JSON string
web_issue_detail_instance = WebIssueDetail.from_json(json)
# print the JSON string representation of the object
print(WebIssueDetail.to_json())

# convert the object into a dict
web_issue_detail_dict = web_issue_detail_instance.to_dict()
# create an instance of WebIssueDetail from a dict
web_issue_detail_from_dict = WebIssueDetail.from_dict(web_issue_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


