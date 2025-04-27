# HandlerCreateIssueCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_create_issue_comment_form import HandlerCreateIssueCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerCreateIssueCommentForm from a JSON string
handler_create_issue_comment_form_instance = HandlerCreateIssueCommentForm.from_json(json)
# print the JSON string representation of the object
print(HandlerCreateIssueCommentForm.to_json())

# convert the object into a dict
handler_create_issue_comment_form_dict = handler_create_issue_comment_form_instance.to_dict()
# create an instance of HandlerCreateIssueCommentForm from a dict
handler_create_issue_comment_form_from_dict = HandlerCreateIssueCommentForm.from_dict(handler_create_issue_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


