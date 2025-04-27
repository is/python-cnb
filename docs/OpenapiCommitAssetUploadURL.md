# OpenapiCommitAssetUploadURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_in_sec** | **int** |  | [optional] 
**upload_url** | **str** |  | [optional] 
**verify_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_commit_asset_upload_url import OpenapiCommitAssetUploadURL

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiCommitAssetUploadURL from a JSON string
openapi_commit_asset_upload_url_instance = OpenapiCommitAssetUploadURL.from_json(json)
# print the JSON string representation of the object
print(OpenapiCommitAssetUploadURL.to_json())

# convert the object into a dict
openapi_commit_asset_upload_url_dict = openapi_commit_asset_upload_url_instance.to_dict()
# create an instance of OpenapiCommitAssetUploadURL from a dict
openapi_commit_asset_upload_url_from_dict = OpenapiCommitAssetUploadURL.from_dict(openapi_commit_asset_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


