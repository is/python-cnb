# ApiPostIssueForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** |  | [optional] 
**body** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**priority** | **str** | Priority of this issue. Can be one of: &#x60;p0&#x60;, &#x60;p1&#x60;, &#x60;p2&#x60;, &#x60;p3&#x60;, &#x60;\&quot;\&quot;&#x60;. | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_post_issue_form import ApiPostIssueForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostIssueForm from a JSON string
api_post_issue_form_instance = ApiPostIssueForm.from_json(json)
# print the JSON string representation of the object
print(ApiPostIssueForm.to_json())

# convert the object into a dict
api_post_issue_form_dict = api_post_issue_form_instance.to_dict()
# create an instance of ApiPostIssueForm from a dict
api_post_issue_form_from_dict = ApiPostIssueForm.from_dict(api_post_issue_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


