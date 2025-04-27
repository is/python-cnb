# WebapiPatchPullRequestAssigneesForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_patch_pull_request_assignees_form import WebapiPatchPullRequestAssigneesForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPatchPullRequestAssigneesForm from a JSON string
webapi_patch_pull_request_assignees_form_instance = WebapiPatchPullRequestAssigneesForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPatchPullRequestAssigneesForm.to_json())

# convert the object into a dict
webapi_patch_pull_request_assignees_form_dict = webapi_patch_pull_request_assignees_form_instance.to_dict()
# create an instance of WebapiPatchPullRequestAssigneesForm from a dict
webapi_patch_pull_request_assignees_form_from_dict = WebapiPatchPullRequestAssigneesForm.from_dict(webapi_patch_pull_request_assignees_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


