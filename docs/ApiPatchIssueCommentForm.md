# ApiPatchIssueCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_patch_issue_comment_form import ApiPatchIssueCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPatchIssueCommentForm from a JSON string
api_patch_issue_comment_form_instance = ApiPatchIssueCommentForm.from_json(json)
# print the JSON string representation of the object
print(ApiPatchIssueCommentForm.to_json())

# convert the object into a dict
api_patch_issue_comment_form_dict = api_patch_issue_comment_form_instance.to_dict()
# create an instance of ApiPatchIssueCommentForm from a dict
api_patch_issue_comment_form_from_dict = ApiPatchIssueCommentForm.from_dict(api_patch_issue_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


