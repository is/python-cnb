# WebapiCreatePullRequestForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** |  | [optional] 
**base_branch** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_repo_slug** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**reviewers** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_create_pull_request_form import WebapiCreatePullRequestForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiCreatePullRequestForm from a JSON string
webapi_create_pull_request_form_instance = WebapiCreatePullRequestForm.from_json(json)
# print the JSON string representation of the object
print(WebapiCreatePullRequestForm.to_json())

# convert the object into a dict
webapi_create_pull_request_form_dict = webapi_create_pull_request_form_instance.to_dict()
# create an instance of WebapiCreatePullRequestForm from a dict
webapi_create_pull_request_form_from_dict = WebapiCreatePullRequestForm.from_dict(webapi_create_pull_request_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


