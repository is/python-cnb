# WebapiCreateIssueCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_create_issue_comment_form import WebapiCreateIssueCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiCreateIssueCommentForm from a JSON string
webapi_create_issue_comment_form_instance = WebapiCreateIssueCommentForm.from_json(json)
# print the JSON string representation of the object
print(WebapiCreateIssueCommentForm.to_json())

# convert the object into a dict
webapi_create_issue_comment_form_dict = webapi_create_issue_comment_form_instance.to_dict()
# create an instance of WebapiCreateIssueCommentForm from a dict
webapi_create_issue_comment_form_from_dict = WebapiCreateIssueCommentForm.from_dict(webapi_create_issue_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


