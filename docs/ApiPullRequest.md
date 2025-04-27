# ApiPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo]**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**base** | [**ApiPullRef**](ApiPullRef.md) |  | [optional] 
**blocked_on** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**head** | [**ApiPullRef**](ApiPullRef.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**merged_by** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**number** | **str** |  | [optional] 
**repo** | [**ApiRepo**](ApiRepo.md) |  | [optional] 
**review_count** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_request import ApiPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRequest from a JSON string
api_pull_request_instance = ApiPullRequest.from_json(json)
# print the JSON string representation of the object
print(ApiPullRequest.to_json())

# convert the object into a dict
api_pull_request_dict = api_pull_request_instance.to_dict()
# create an instance of ApiPullRequest from a dict
api_pull_request_from_dict = ApiPullRequest.from_dict(api_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


