# WebGitUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_object_size_limit_in_kib** | **str** |  | [optional] 
**git_quota_in_kib** | **str** |  | [optional] 
**git_used_in_kib** | **str** |  | [optional] 
**lfs_limit_in_kib** | **str** | deprecated | [optional] 
**lfs_object_size_limit_in_kib** | **str** |  | [optional] 
**lfs_quota_in_kib** | **str** |  | [optional] 
**lfs_used_in_kib** | **str** |  | [optional] 
**limit_in_kib** | **str** | deprecated | [optional] 
**logical_lfs_used_in_kib** | **str** |  | [optional] 
**max_git_object_size_limit_in_kib** | **str** |  | [optional] 
**max_lfs_object_size_limit_in_kib** | **str** |  | [optional] 
**physical_lfs_used_in_kib** | **str** |  | [optional] 
**used_in_kib** | **str** | deprecated | [optional] 

## Example

```python
from cnb_api.models.web_git_usage import WebGitUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WebGitUsage from a JSON string
web_git_usage_instance = WebGitUsage.from_json(json)
# print the JSON string representation of the object
print(WebGitUsage.to_json())

# convert the object into a dict
web_git_usage_dict = web_git_usage_instance.to_dict()
# create an instance of WebGitUsage from a dict
web_git_usage_from_dict = WebGitUsage.from_dict(web_git_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


