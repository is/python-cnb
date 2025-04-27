# WebPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**base_repo_ref** | **str** |  | [optional] 
**blocked_on** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commit_statuses** | [**WebCommitStatuses**](WebCommitStatuses.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**file_count** | **int** |  | [optional] 
**head_deleted** | **bool** |  | [optional] 
**head_repo_ref** | **str** |  | [optional] 
**head_repo_slug** | **str** |  | [optional] 
**is_merged** | **bool** |  | [optional] 
**is_ready_for_merge** | **bool** |  | [optional] 
**labels** | [**List[LabelOption]**](LabelOption.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**merge_style** | **str** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**review_comment_count** | **int** |  | [optional] 
**review_count** | **int** |  | [optional] 
**reviewers** | [**List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status_check_commit_sha** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request import WebPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequest from a JSON string
web_pull_request_instance = WebPullRequest.from_json(json)
# print the JSON string representation of the object
print(WebPullRequest.to_json())

# convert the object into a dict
web_pull_request_dict = web_pull_request_instance.to_dict()
# create an instance of WebPullRequest from a dict
web_pull_request_from_dict = WebPullRequest.from_dict(web_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


