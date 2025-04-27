# WebIssueComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**author_meta** | **List[int]** |  | [optional] 
**body** | **str** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_comment import WebIssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueComment from a JSON string
web_issue_comment_instance = WebIssueComment.from_json(json)
# print the JSON string representation of the object
print(WebIssueComment.to_json())

# convert the object into a dict
web_issue_comment_dict = web_issue_comment_instance.to_dict()
# create an instance of WebIssueComment from a dict
web_issue_comment_from_dict = WebIssueComment.from_dict(web_issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


