# DtoResourceRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_policy** | **str** |  | [optional] [default to 'all']
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**last_push_time** | **str** |  | [optional] 
**last_push_user** | [**DtoUsers**](DtoUsers.md) |  | [optional] 
**name** | **str** |  | [optional] 
**overwrite_policy** | **str** |  | [optional] [default to 'forbid']
**path** | **str** |  | [optional] 
**pkg_count** | **int** |  | [optional] [readonly] 
**updated_at** | **str** |  | [optional] 
**used_size** | **int** |  | [optional] [readonly] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_resource_registry import DtoResourceRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResourceRegistry from a JSON string
dto_resource_registry_instance = DtoResourceRegistry.from_json(json)
# print the JSON string representation of the object
print(DtoResourceRegistry.to_json())

# convert the object into a dict
dto_resource_registry_dict = dto_resource_registry_instance.to_dict()
# create an instance of DtoResourceRegistry from a dict
dto_resource_registry_from_dict = DtoResourceRegistry.from_dict(dto_resource_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


