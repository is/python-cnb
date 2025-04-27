# DtoSystemAcceleration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_system_acceleration import DtoSystemAcceleration

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSystemAcceleration from a JSON string
dto_system_acceleration_instance = DtoSystemAcceleration.from_json(json)
# print the JSON string representation of the object
print(DtoSystemAcceleration.to_json())

# convert the object into a dict
dto_system_acceleration_dict = dto_system_acceleration_instance.to_dict()
# create an instance of DtoSystemAcceleration from a dict
dto_system_acceleration_from_dict = DtoSystemAcceleration.from_dict(dto_system_acceleration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


