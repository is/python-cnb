# DtoResourceMission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_resource_mission import DtoResourceMission

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResourceMission from a JSON string
dto_resource_mission_instance = DtoResourceMission.from_json(json)
# print the JSON string representation of the object
print(DtoResourceMission.to_json())

# convert the object into a dict
dto_resource_mission_dict = dto_resource_mission_instance.to_dict()
# create an instance of DtoResourceMission from a dict
dto_resource_mission_from_dict = DtoResourceMission.from_dict(dto_resource_mission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


