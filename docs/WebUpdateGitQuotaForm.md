# WebUpdateGitQuotaForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_object_size_limit_in_kib** | **str** |  | [optional] 
**git_quota_in_kib** | **str** |  | [optional] 
**quota_in_kib** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_update_git_quota_form import WebUpdateGitQuotaForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebUpdateGitQuotaForm from a JSON string
web_update_git_quota_form_instance = WebUpdateGitQuotaForm.from_json(json)
# print the JSON string representation of the object
print(WebUpdateGitQuotaForm.to_json())

# convert the object into a dict
web_update_git_quota_form_dict = web_update_git_quota_form_instance.to_dict()
# create an instance of WebUpdateGitQuotaForm from a dict
web_update_git_quota_form_from_dict = WebUpdateGitQuotaForm.from_dict(web_update_git_quota_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


