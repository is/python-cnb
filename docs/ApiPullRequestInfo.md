# ApiPullRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo]**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**base** | [**ApiPullRefInfo**](ApiPullRefInfo.md) |  | [optional] 
**blocked_on** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**head** | [**ApiPullRefInfo**](ApiPullRefInfo.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**merged_by** | [**GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**number** | **str** |  | [optional] 
**repo** | [**ApiRepoInfo**](ApiRepoInfo.md) |  | [optional] 
**reviewers** | [**List[GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo]**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_request_info import ApiPullRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRequestInfo from a JSON string
api_pull_request_info_instance = ApiPullRequestInfo.from_json(json)
# print the JSON string representation of the object
print(ApiPullRequestInfo.to_json())

# convert the object into a dict
api_pull_request_info_dict = api_pull_request_info_instance.to_dict()
# create an instance of ApiPullRequestInfo from a dict
api_pull_request_info_from_dict = ApiPullRequestInfo.from_dict(api_pull_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


