# WebPullRequestState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_statuses** | [**WebCommitStatuses**](WebCommitStatuses.md) |  | [optional] 
**merge_style** | **str** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**reviews** | [**WebPullRequestReviews**](WebPullRequestReviews.md) |  | [optional] 
**settings** | [**WebPullRequestSetting**](WebPullRequestSetting.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status_check_commit_sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_state import WebPullRequestState

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestState from a JSON string
web_pull_request_state_instance = WebPullRequestState.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestState.to_json())

# convert the object into a dict
web_pull_request_state_dict = web_pull_request_state_instance.to_dict()
# create an instance of WebPullRequestState from a dict
web_pull_request_state_from_dict = WebPullRequestState.from_dict(web_pull_request_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


