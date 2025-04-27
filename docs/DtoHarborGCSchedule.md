# DtoHarborGCSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** |  | [optional] 
**last_triggered_time** | **str** |  | [optional] 
**next_scheduled_time** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_harbor_gc_schedule import DtoHarborGCSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DtoHarborGCSchedule from a JSON string
dto_harbor_gc_schedule_instance = DtoHarborGCSchedule.from_json(json)
# print the JSON string representation of the object
print(DtoHarborGCSchedule.to_json())

# convert the object into a dict
dto_harbor_gc_schedule_dict = dto_harbor_gc_schedule_instance.to_dict()
# create an instance of DtoHarborGCSchedule from a dict
dto_harbor_gc_schedule_from_dict = DtoHarborGCSchedule.from_dict(dto_harbor_gc_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


