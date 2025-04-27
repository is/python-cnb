# WebapiPostPullRequestReviewReplyForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**reply_to_comment_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_pull_request_review_reply_form import WebapiPostPullRequestReviewReplyForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostPullRequestReviewReplyForm from a JSON string
webapi_post_pull_request_review_reply_form_instance = WebapiPostPullRequestReviewReplyForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostPullRequestReviewReplyForm.to_json())

# convert the object into a dict
webapi_post_pull_request_review_reply_form_dict = webapi_post_pull_request_review_reply_form_instance.to_dict()
# create an instance of WebapiPostPullRequestReviewReplyForm from a dict
webapi_post_pull_request_review_reply_form_from_dict = WebapiPostPullRequestReviewReplyForm.from_dict(webapi_post_pull_request_review_reply_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


