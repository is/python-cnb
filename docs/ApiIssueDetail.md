# ApiIssueDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo]**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**labels** | [**List[ApiLabel]**](ApiLabel.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_reason** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_issue_detail import ApiIssueDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIssueDetail from a JSON string
api_issue_detail_instance = ApiIssueDetail.from_json(json)
# print the JSON string representation of the object
print(ApiIssueDetail.to_json())

# convert the object into a dict
api_issue_detail_dict = api_issue_detail_instance.to_dict()
# create an instance of ApiIssueDetail from a dict
api_issue_detail_from_dict = ApiIssueDetail.from_dict(api_issue_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


