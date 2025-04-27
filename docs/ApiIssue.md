# ApiIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo]**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
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
from cnb_api.models.api_issue import ApiIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIssue from a JSON string
api_issue_instance = ApiIssue.from_json(json)
# print the JSON string representation of the object
print(ApiIssue.to_json())

# convert the object into a dict
api_issue_dict = api_issue_instance.to_dict()
# create an instance of ApiIssue from a dict
api_issue_from_dict = ApiIssue.from_dict(api_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


