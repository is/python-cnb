# DtoTimeVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_rfc3339** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_time_volume import DtoTimeVolume

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTimeVolume from a JSON string
dto_time_volume_instance = DtoTimeVolume.from_json(json)
# print the JSON string representation of the object
print(DtoTimeVolume.to_json())

# convert the object into a dict
dto_time_volume_dict = dto_time_volume_instance.to_dict()
# create an instance of DtoTimeVolume from a dict
dto_time_volume_from_dict = DtoTimeVolume.from_dict(dto_time_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


