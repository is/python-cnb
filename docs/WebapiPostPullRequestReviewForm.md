# WebapiPostPullRequestReviewForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**comment** | [**WebapiPostPullRequestReviewCommentForm**](WebapiPostPullRequestReviewCommentForm.md) |  | [optional] 
**event** | **str** | comment, approve, request_changes or \&quot;\&quot; | [optional] 

## Example

```python
from cnb_api.models.webapi_post_pull_request_review_form import WebapiPostPullRequestReviewForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostPullRequestReviewForm from a JSON string
webapi_post_pull_request_review_form_instance = WebapiPostPullRequestReviewForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostPullRequestReviewForm.to_json())

# convert the object into a dict
webapi_post_pull_request_review_form_dict = webapi_post_pull_request_review_form_instance.to_dict()
# create an instance of WebapiPostPullRequestReviewForm from a dict
webapi_post_pull_request_review_form_from_dict = WebapiPostPullRequestReviewForm.from_dict(webapi_post_pull_request_review_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


