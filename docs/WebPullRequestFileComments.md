# WebPullRequestFileComments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[WebPullRequestReviewComment]**](WebPullRequestReviewComment.md) |  | [optional] 
**path** | **str** |  | [optional] 
**total_comment** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_file_comments import WebPullRequestFileComments

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestFileComments from a JSON string
web_pull_request_file_comments_instance = WebPullRequestFileComments.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestFileComments.to_json())

# convert the object into a dict
web_pull_request_file_comments_dict = web_pull_request_file_comments_instance.to_dict()
# create an instance of WebPullRequestFileComments from a dict
web_pull_request_file_comments_from_dict = WebPullRequestFileComments.from_dict(web_pull_request_file_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


