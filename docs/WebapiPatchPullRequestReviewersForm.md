# WebapiPatchPullRequestReviewersForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_patch_pull_request_reviewers_form import WebapiPatchPullRequestReviewersForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPatchPullRequestReviewersForm from a JSON string
webapi_patch_pull_request_reviewers_form_instance = WebapiPatchPullRequestReviewersForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPatchPullRequestReviewersForm.to_json())

# convert the object into a dict
webapi_patch_pull_request_reviewers_form_dict = webapi_patch_pull_request_reviewers_form_instance.to_dict()
# create an instance of WebapiPatchPullRequestReviewersForm from a dict
webapi_patch_pull_request_reviewers_form_from_dict = WebapiPatchPullRequestReviewersForm.from_dict(webapi_patch_pull_request_reviewers_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


