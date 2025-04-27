# WebMissionField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_type** | [**DtoInteractionType**](DtoInteractionType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **List[object]** |  | [optional] 

## Example

```python
from cnb_api.models.web_mission_field import WebMissionField

# TODO update the JSON string below
json = "{}"
# create an instance of WebMissionField from a JSON string
web_mission_field_instance = WebMissionField.from_json(json)
# print the JSON string representation of the object
print(WebMissionField.to_json())

# convert the object into a dict
web_mission_field_dict = web_mission_field_instance.to_dict()
# create an instance of WebMissionField from a dict
web_mission_field_from_dict = WebMissionField.from_dict(web_mission_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


