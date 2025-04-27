# WebapiPostCommitForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_branch** | **str** |  | [optional] 
**files** | [**List[WebapiPostCommitFile]**](WebapiPostCommitFile.md) |  | [optional] 
**message** | **str** |  | [optional] 
**new_branch** | **str** |  | [optional] 
**parent_commit_sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_commit_form import WebapiPostCommitForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostCommitForm from a JSON string
webapi_post_commit_form_instance = WebapiPostCommitForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostCommitForm.to_json())

# convert the object into a dict
webapi_post_commit_form_dict = webapi_post_commit_form_instance.to_dict()
# create an instance of WebapiPostCommitForm from a dict
webapi_post_commit_form_from_dict = WebapiPostCommitForm.from_dict(webapi_post_commit_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


