# WebPullRequestReviewComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**author_meta** | **List[int]** |  | [optional] 
**body** | **str** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**commit_hash** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**diff_hunk** | [**List[WebDiffLine]**](WebDiffLine.md) |  | [optional] 
**end_line** | **int** |  | [optional] 
**end_side** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**replies** | [**List[WebPullRequestReviewCommentReply]**](WebPullRequestReviewCommentReply.md) |  | [optional] 
**reply_to_comment_id** | **str** |  | [optional] 
**review_id** | **str** |  | [optional] 
**start_line** | **int** |  | [optional] 
**start_side** | **str** |  | [optional] 
**subject_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_review_comment import WebPullRequestReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestReviewComment from a JSON string
web_pull_request_review_comment_instance = WebPullRequestReviewComment.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestReviewComment.to_json())

# convert the object into a dict
web_pull_request_review_comment_dict = web_pull_request_review_comment_instance.to_dict()
# create an instance of WebPullRequestReviewComment from a dict
web_pull_request_review_comment_from_dict = WebPullRequestReviewComment.from_dict(web_pull_request_review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


