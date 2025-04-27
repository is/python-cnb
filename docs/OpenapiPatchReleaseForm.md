# OpenapiPatchReleaseForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**make_latest** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_patch_release_form import OpenapiPatchReleaseForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiPatchReleaseForm from a JSON string
openapi_patch_release_form_instance = OpenapiPatchReleaseForm.from_json(json)
# print the JSON string representation of the object
print(OpenapiPatchReleaseForm.to_json())

# convert the object into a dict
openapi_patch_release_form_dict = openapi_patch_release_form_instance.to_dict()
# create an instance of OpenapiPatchReleaseForm from a dict
openapi_patch_release_form_from_dict = OpenapiPatchReleaseForm.from_dict(openapi_patch_release_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


