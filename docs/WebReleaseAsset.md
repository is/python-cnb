# WebReleaseAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**content_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size_in_byte** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_release_asset import WebReleaseAsset

# TODO update the JSON string below
json = "{}"
# create an instance of WebReleaseAsset from a JSON string
web_release_asset_instance = WebReleaseAsset.from_json(json)
# print the JSON string representation of the object
print(WebReleaseAsset.to_json())

# convert the object into a dict
web_release_asset_dict = web_release_asset_instance.to_dict()
# create an instance of WebReleaseAsset from a dict
web_release_asset_from_dict = WebReleaseAsset.from_dict(web_release_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


