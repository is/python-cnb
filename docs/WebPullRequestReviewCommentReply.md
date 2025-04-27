# WebPullRequestReviewCommentReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_review_comment_reply import WebPullRequestReviewCommentReply

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestReviewCommentReply from a JSON string
web_pull_request_review_comment_reply_instance = WebPullRequestReviewCommentReply.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestReviewCommentReply.to_json())

# convert the object into a dict
web_pull_request_review_comment_reply_dict = web_pull_request_review_comment_reply_instance.to_dict()
# create an instance of WebPullRequestReviewCommentReply from a dict
web_pull_request_review_comment_reply_from_dict = WebPullRequestReviewCommentReply.from_dict(web_pull_request_review_comment_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


