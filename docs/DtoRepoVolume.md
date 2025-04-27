# DtoRepoVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**resource_type** | [**ConstantSlugType**](ConstantSlugType.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_repo_volume import DtoRepoVolume

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepoVolume from a JSON string
dto_repo_volume_instance = DtoRepoVolume.from_json(json)
# print the JSON string representation of the object
print(DtoRepoVolume.to_json())

# convert the object into a dict
dto_repo_volume_dict = dto_repo_volume_instance.to_dict()
# create an instance of DtoRepoVolume from a dict
dto_repo_volume_from_dict = DtoRepoVolume.from_dict(dto_repo_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


