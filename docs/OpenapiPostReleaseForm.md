# OpenapiPostReleaseForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**make_latest** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_post_release_form import OpenapiPostReleaseForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiPostReleaseForm from a JSON string
openapi_post_release_form_instance = OpenapiPostReleaseForm.from_json(json)
# print the JSON string representation of the object
print(OpenapiPostReleaseForm.to_json())

# convert the object into a dict
openapi_post_release_form_dict = openapi_post_release_form_instance.to_dict()
# create an instance of OpenapiPostReleaseForm from a dict
openapi_post_release_form_from_dict = OpenapiPostReleaseForm.from_dict(openapi_post_release_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


