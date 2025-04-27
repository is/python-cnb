# ApiPull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**ApiPullRef**](ApiPullRef.md) |  | [optional] 
**body** | **str** |  | [optional] 
**head** | [**ApiPullRef**](ApiPullRef.md) |  | [optional] 
**merged_by** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**number** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull import ApiPull

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPull from a JSON string
api_pull_instance = ApiPull.from_json(json)
# print the JSON string representation of the object
print(ApiPull.to_json())

# convert the object into a dict
api_pull_dict = api_pull_instance.to_dict()
# create an instance of ApiPull from a dict
api_pull_from_dict = ApiPull.from_dict(api_pull_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


