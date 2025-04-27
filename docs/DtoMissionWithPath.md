# DtoMissionWithPath


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
from cnb_api.models.dto_mission_with_path import DtoMissionWithPath

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMissionWithPath from a JSON string
dto_mission_with_path_instance = DtoMissionWithPath.from_json(json)
# print the JSON string representation of the object
print(DtoMissionWithPath.to_json())

# convert the object into a dict
dto_mission_with_path_dict = dto_mission_with_path_instance.to_dict()
# create an instance of DtoMissionWithPath from a dict
dto_mission_with_path_from_dict = DtoMissionWithPath.from_dict(dto_mission_with_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


