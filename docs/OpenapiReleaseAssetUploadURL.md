# OpenapiReleaseAssetUploadURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in_sec** | **int** |  | [optional] 
**upload_url** | **str** |  | [optional] 
**verify_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_release_asset_upload_url import OpenapiReleaseAssetUploadURL

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiReleaseAssetUploadURL from a JSON string
openapi_release_asset_upload_url_instance = OpenapiReleaseAssetUploadURL.from_json(json)
# print the JSON string representation of the object
print(OpenapiReleaseAssetUploadURL.to_json())

# convert the object into a dict
openapi_release_asset_upload_url_dict = openapi_release_asset_upload_url_instance.to_dict()
# create an instance of OpenapiReleaseAssetUploadURL from a dict
openapi_release_asset_upload_url_from_dict = OpenapiReleaseAssetUploadURL.from_dict(openapi_release_asset_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


