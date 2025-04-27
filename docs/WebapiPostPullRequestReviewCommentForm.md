# WebapiPostPullRequestReviewCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**end_line** | **int** |  | [optional] 
**end_side** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start_line** | **int** |  | [optional] 
**start_side** | **str** |  | [optional] 
**subject_type** | **str** | can be one of: line, file | [optional] 

## Example

```python
from cnb_api.models.webapi_post_pull_request_review_comment_form import WebapiPostPullRequestReviewCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostPullRequestReviewCommentForm from a JSON string
webapi_post_pull_request_review_comment_form_instance = WebapiPostPullRequestReviewCommentForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostPullRequestReviewCommentForm.to_json())

# convert the object into a dict
webapi_post_pull_request_review_comment_form_dict = webapi_post_pull_request_review_comment_form_instance.to_dict()
# create an instance of WebapiPostPullRequestReviewCommentForm from a dict
webapi_post_pull_request_review_comment_form_from_dict = WebapiPostPullRequestReviewCommentForm.from_dict(webapi_post_pull_request_review_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


