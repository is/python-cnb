# WebPullRequestResourceReviewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** |  | [optional] 
**review_state** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_resource_reviewer import WebPullRequestResourceReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestResourceReviewer from a JSON string
web_pull_request_resource_reviewer_instance = WebPullRequestResourceReviewer.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestResourceReviewer.to_json())

# convert the object into a dict
web_pull_request_resource_reviewer_dict = web_pull_request_resource_reviewer_instance.to_dict()
# create an instance of WebPullRequestResourceReviewer from a dict
web_pull_request_resource_reviewer_from_dict = WebPullRequestResourceReviewer.from_dict(web_pull_request_resource_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


