# WebRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[WebReleaseAsset]**](WebReleaseAsset.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**is_latest** | **bool** |  | [optional] 
**is_prerelease** | **bool** |  | [optional] 
**last_updated_by** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 
**published_at** | **str** |  | [optional] 
**tag_ref** | **str** |  | [optional] 
**target_commit_hash** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_release import WebRelease

# TODO update the JSON string below
json = "{}"
# create an instance of WebRelease from a JSON string
web_release_instance = WebRelease.from_json(json)
# print the JSON string representation of the object
print(WebRelease.to_json())

# convert the object into a dict
web_release_dict = web_release_instance.to_dict()
# create an instance of WebRelease from a dict
web_release_from_dict = WebRelease.from_dict(web_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


