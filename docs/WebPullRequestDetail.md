# WebPullRequestDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_merge_styles** | **List[str]** |  | [optional] 
**assignees** | [**List[WebPullRequestAssignee]**](WebPullRequestAssignee.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**base** | [**WebPullRequestRepository**](WebPullRequestRepository.md) |  | [optional] 
**base_repo_ref** | **str** |  | [optional] 
**blocked_on** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**can_do_merge** | **bool** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commit_statuses** | [**WebCommitStatuses**](WebCommitStatuses.md) |  | [optional] 
**conflict_file_count** | **int** |  | [optional] 
**conflict_files** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**file_count** | **int** |  | [optional] 
**head** | [**WebPullRequestRepository**](WebPullRequestRepository.md) |  | [optional] 
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
**participants** | [**List[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo]**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**review_comment_count** | **int** |  | [optional] 
**review_count** | **int** |  | [optional] 
**reviewers** | [**List[WebPullRequestReviewer]**](WebPullRequestReviewer.md) |  | [optional] 
**reviews** | [**WebPullRequestReviews**](WebPullRequestReviews.md) |  | [optional] 
**settings** | [**WebPullRequestSetting**](WebPullRequestSetting.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status_check_commit_sha** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_detail import WebPullRequestDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestDetail from a JSON string
web_pull_request_detail_instance = WebPullRequestDetail.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestDetail.to_json())

# convert the object into a dict
web_pull_request_detail_dict = web_pull_request_detail_instance.to_dict()
# create an instance of WebPullRequestDetail from a dict
web_pull_request_detail_from_dict = WebPullRequestDetail.from_dict(web_pull_request_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


