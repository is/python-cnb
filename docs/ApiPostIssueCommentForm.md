# ApiPostIssueCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_post_issue_comment_form import ApiPostIssueCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostIssueCommentForm from a JSON string
api_post_issue_comment_form_instance = ApiPostIssueCommentForm.from_json(json)
# print the JSON string representation of the object
print(ApiPostIssueCommentForm.to_json())

# convert the object into a dict
api_post_issue_comment_form_dict = api_post_issue_comment_form_instance.to_dict()
# create an instance of ApiPostIssueCommentForm from a dict
api_post_issue_comment_form_from_dict = ApiPostIssueCommentForm.from_dict(api_post_issue_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


