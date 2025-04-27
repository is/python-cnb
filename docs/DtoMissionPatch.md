# DtoMissionPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**ref_repos** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.dto_mission_patch import DtoMissionPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMissionPatch from a JSON string
dto_mission_patch_instance = DtoMissionPatch.from_json(json)
# print the JSON string representation of the object
print(DtoMissionPatch.to_json())

# convert the object into a dict
dto_mission_patch_dict = dto_mission_patch_instance.to_dict()
# create an instance of DtoMissionPatch from a dict
dto_mission_patch_from_dict = DtoMissionPatch.from_dict(dto_mission_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


