# ApiReleaseAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uploader** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.api_release_asset import ApiReleaseAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReleaseAsset from a JSON string
api_release_asset_instance = ApiReleaseAsset.from_json(json)
# print the JSON string representation of the object
print(ApiReleaseAsset.to_json())

# convert the object into a dict
api_release_asset_dict = api_release_asset_instance.to_dict()
# create an instance of ApiReleaseAsset from a dict
api_release_asset_from_dict = ApiReleaseAsset.from_dict(api_release_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


