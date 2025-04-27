# HandlerUpdateIssueForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**priority** | **str** | p0, p1, p2, p3, \&quot;\&quot;。 single choice。 | [optional] 
**start_date** | **str** |  | [optional] 
**state** | **str** | open or closed | [optional] 
**state_reason** | **str** | completed, not_planned, reopened | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_update_issue_form import HandlerUpdateIssueForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerUpdateIssueForm from a JSON string
handler_update_issue_form_instance = HandlerUpdateIssueForm.from_json(json)
# print the JSON string representation of the object
print(HandlerUpdateIssueForm.to_json())

# convert the object into a dict
handler_update_issue_form_dict = handler_update_issue_form_instance.to_dict()
# create an instance of HandlerUpdateIssueForm from a dict
handler_update_issue_form_from_dict = HandlerUpdateIssueForm.from_dict(handler_update_issue_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


