# WebPullRequestReviewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_state** | **str** |  | [optional] 
**user** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_reviewer import WebPullRequestReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestReviewer from a JSON string
web_pull_request_reviewer_instance = WebPullRequestReviewer.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestReviewer.to_json())

# convert the object into a dict
web_pull_request_reviewer_dict = web_pull_request_reviewer_instance.to_dict()
# create an instance of WebPullRequestReviewer from a dict
web_pull_request_reviewer_from_dict = WebPullRequestReviewer.from_dict(web_pull_request_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


