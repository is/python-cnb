# WebPullRequestActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**actor_access_role** | **str** |  | [optional] 
**actor_meta** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_activity import WebPullRequestActivity

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestActivity from a JSON string
web_pull_request_activity_instance = WebPullRequestActivity.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestActivity.to_json())

# convert the object into a dict
web_pull_request_activity_dict = web_pull_request_activity_instance.to_dict()
# create an instance of WebPullRequestActivity from a dict
web_pull_request_activity_from_dict = WebPullRequestActivity.from_dict(web_pull_request_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


