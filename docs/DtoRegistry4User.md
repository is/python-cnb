# DtoRegistry4User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
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
**star_time** | **str** |  | [optional] 
**stared** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**used_size** | **int** |  | [optional] [readonly] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_registry4_user import DtoRegistry4User

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRegistry4User from a JSON string
dto_registry4_user_instance = DtoRegistry4User.from_json(json)
# print the JSON string representation of the object
print(DtoRegistry4User.to_json())

# convert the object into a dict
dto_registry4_user_dict = dto_registry4_user_instance.to_dict()
# create an instance of DtoRegistry4User from a dict
dto_registry4_user_from_dict = DtoRegistry4User.from_dict(dto_registry4_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


