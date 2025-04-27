# WebCommitAsset


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
from cnb_api.models.web_commit_asset import WebCommitAsset

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitAsset from a JSON string
web_commit_asset_instance = WebCommitAsset.from_json(json)
# print the JSON string representation of the object
print(WebCommitAsset.to_json())

# convert the object into a dict
web_commit_asset_dict = web_commit_asset_instance.to_dict()
# create an instance of WebCommitAsset from a dict
web_commit_asset_from_dict = WebCommitAsset.from_dict(web_commit_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


