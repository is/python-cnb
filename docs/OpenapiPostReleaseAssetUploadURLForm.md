# OpenapiPostReleaseAssetUploadURLForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_name** | **str** |  | [optional] 
**overwrite** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_post_release_asset_upload_url_form import OpenapiPostReleaseAssetUploadURLForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiPostReleaseAssetUploadURLForm from a JSON string
openapi_post_release_asset_upload_url_form_instance = OpenapiPostReleaseAssetUploadURLForm.from_json(json)
# print the JSON string representation of the object
print(OpenapiPostReleaseAssetUploadURLForm.to_json())

# convert the object into a dict
openapi_post_release_asset_upload_url_form_dict = openapi_post_release_asset_upload_url_form_instance.to_dict()
# create an instance of OpenapiPostReleaseAssetUploadURLForm from a dict
openapi_post_release_asset_upload_url_form_from_dict = OpenapiPostReleaseAssetUploadURLForm.from_dict(openapi_post_release_asset_upload_url_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


