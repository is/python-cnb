# WebPullRequestReviews


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_ratio** | **int** |  | [optional] 
**master_reviewers** | [**List[WebPullRequestReviewer]**](WebPullRequestReviewer.md) |  | [optional] 
**reviewers** | [**List[WebPullRequestReviewer]**](WebPullRequestReviewer.md) |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_reviews import WebPullRequestReviews

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestReviews from a JSON string
web_pull_request_reviews_instance = WebPullRequestReviews.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestReviews.to_json())

# convert the object into a dict
web_pull_request_reviews_dict = web_pull_request_reviews_instance.to_dict()
# create an instance of WebPullRequestReviews from a dict
web_pull_request_reviews_from_dict = WebPullRequestReviews.from_dict(web_pull_request_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


