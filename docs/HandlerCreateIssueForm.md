# HandlerCreateIssueForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** |  | [optional] 
**body** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**priority** | **str** | p0, p1, p2, p3, \&quot;\&quot;。 single choice。 | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_create_issue_form import HandlerCreateIssueForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerCreateIssueForm from a JSON string
handler_create_issue_form_instance = HandlerCreateIssueForm.from_json(json)
# print the JSON string representation of the object
print(HandlerCreateIssueForm.to_json())

# convert the object into a dict
handler_create_issue_form_dict = handler_create_issue_form_instance.to_dict()
# create an instance of HandlerCreateIssueForm from a dict
handler_create_issue_form_from_dict = HandlerCreateIssueForm.from_dict(handler_create_issue_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


