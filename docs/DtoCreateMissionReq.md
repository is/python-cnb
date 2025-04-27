# DtoCreateMissionReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repos** | **List[str]** |  | [optional] 
**visibility** | **str** |  | [optional] [default to 'public']

## Example

```python
from cnb_api.models.dto_create_mission_req import DtoCreateMissionReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateMissionReq from a JSON string
dto_create_mission_req_instance = DtoCreateMissionReq.from_json(json)
# print the JSON string representation of the object
print(DtoCreateMissionReq.to_json())

# convert the object into a dict
dto_create_mission_req_dict = dto_create_mission_req_instance.to_dict()
# create an instance of DtoCreateMissionReq from a dict
dto_create_mission_req_from_dict = DtoCreateMissionReq.from_dict(dto_create_mission_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


