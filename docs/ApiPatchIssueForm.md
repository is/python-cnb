# ApiPatchIssueForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**priority** | **str** | Priority of this issue. Can be one of: &#x60;p0&#x60;, &#x60;p1&#x60;, &#x60;p2&#x60;, &#x60;p3&#x60;, &#x60;\&quot;\&quot;&#x60;. | [optional] 
**state** | **str** | State of this issue. Either &#x60;open&#x60; or &#x60;closed&#x60;. | [optional] 
**state_reason** | **str** | StateReason can be one of: &#x60;completed&#x60;, &#x60;not_planned&#x60;, &#x60;reopened&#x60; | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_patch_issue_form import ApiPatchIssueForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPatchIssueForm from a JSON string
api_patch_issue_form_instance = ApiPatchIssueForm.from_json(json)
# print the JSON string representation of the object
print(ApiPatchIssueForm.to_json())

# convert the object into a dict
api_patch_issue_form_dict = api_patch_issue_form_instance.to_dict()
# create an instance of ApiPatchIssueForm from a dict
api_patch_issue_form_from_dict = ApiPatchIssueForm.from_dict(api_patch_issue_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


