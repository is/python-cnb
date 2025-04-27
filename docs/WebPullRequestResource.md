# WebPullRequestResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo]**](GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo**](GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo.md) |  | [optional] 
**base_repo_ref** | **str** |  | [optional] 
**blocked_on** | **str** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**customer_fields** | [**List[WebCustomerField]**](WebCustomerField.md) |  | [optional] 
**file_count** | **int** |  | [optional] 
**head_repo_ref** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_merged** | **bool** |  | [optional] 
**is_ready_for_merge** | **bool** |  | [optional] 
**labels** | [**List[WebLabelOption]**](WebLabelOption.md) |  | [optional] 
**last_acted_at** | **str** |  | [optional] 
**merge_style** | **str** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**repo_slug** | **str** |  | [optional] 
**reviewers** | [**List[WebPullRequestResourceReviewer]**](WebPullRequestResourceReviewer.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status_check_commit_sha** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_resource import WebPullRequestResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestResource from a JSON string
web_pull_request_resource_instance = WebPullRequestResource.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestResource.to_json())

# convert the object into a dict
web_pull_request_resource_dict = web_pull_request_resource_instance.to_dict()
# create an instance of WebPullRequestResource from a dict
web_pull_request_resource_from_dict = WebPullRequestResource.from_dict(web_pull_request_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


