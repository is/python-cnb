# WebapiPatchReleaseForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**is_prerelease** | **bool** |  | [optional] 
**make_latest** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_patch_release_form import WebapiPatchReleaseForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPatchReleaseForm from a JSON string
webapi_patch_release_form_instance = WebapiPatchReleaseForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPatchReleaseForm.to_json())

# convert the object into a dict
webapi_patch_release_form_dict = webapi_patch_release_form_instance.to_dict()
# create an instance of WebapiPatchReleaseForm from a dict
webapi_patch_release_form_from_dict = WebapiPatchReleaseForm.from_dict(webapi_patch_release_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


