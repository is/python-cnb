# ApiRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[ApiReleaseAsset]**](ApiReleaseAsset.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_latest** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**published_at** | **str** |  | [optional] 
**tag_commitish** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_release import ApiRelease

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRelease from a JSON string
api_release_instance = ApiRelease.from_json(json)
# print the JSON string representation of the object
print(ApiRelease.to_json())

# convert the object into a dict
api_release_dict = api_release_instance.to_dict()
# create an instance of ApiRelease from a dict
api_release_from_dict = ApiRelease.from_dict(api_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


