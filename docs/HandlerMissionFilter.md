# HandlerMissionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | 属性名 | [optional] 
**operator** | **str** | 筛选符 | [optional] 
**value** | **List[str]** | 属性值 | [optional] 

## Example

```python
from cnb_api.models.handler_mission_filter import HandlerMissionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerMissionFilter from a JSON string
handler_mission_filter_instance = HandlerMissionFilter.from_json(json)
# print the JSON string representation of the object
print(HandlerMissionFilter.to_json())

# convert the object into a dict
handler_mission_filter_dict = handler_mission_filter_instance.to_dict()
# create an instance of HandlerMissionFilter from a dict
handler_mission_filter_from_dict = HandlerMissionFilter.from_dict(handler_mission_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


