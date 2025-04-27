# WebapiMergePullRequestForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_message** | **str** |  | [optional] 
**merge_style** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_merge_pull_request_form import WebapiMergePullRequestForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiMergePullRequestForm from a JSON string
webapi_merge_pull_request_form_instance = WebapiMergePullRequestForm.from_json(json)
# print the JSON string representation of the object
print(WebapiMergePullRequestForm.to_json())

# convert the object into a dict
webapi_merge_pull_request_form_dict = webapi_merge_pull_request_form_instance.to_dict()
# create an instance of WebapiMergePullRequestForm from a dict
webapi_merge_pull_request_form_from_dict = WebapiMergePullRequestForm.from_dict(webapi_merge_pull_request_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


