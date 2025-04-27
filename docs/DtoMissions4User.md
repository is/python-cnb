# DtoMissions4User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**star_time** | **str** |  | [optional] 
**stared** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_missions4_user import DtoMissions4User

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMissions4User from a JSON string
dto_missions4_user_instance = DtoMissions4User.from_json(json)
# print the JSON string representation of the object
print(DtoMissions4User.to_json())

# convert the object into a dict
dto_missions4_user_dict = dto_missions4_user_instance.to_dict()
# create an instance of DtoMissions4User from a dict
dto_missions4_user_from_dict = DtoMissions4User.from_dict(dto_missions4_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


