# DtoAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_msg** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**expired_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**pinned** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_announcement import DtoAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAnnouncement from a JSON string
dto_announcement_instance = DtoAnnouncement.from_json(json)
# print the JSON string representation of the object
print(DtoAnnouncement.to_json())

# convert the object into a dict
dto_announcement_dict = dto_announcement_instance.to_dict()
# create an instance of DtoAnnouncement from a dict
dto_announcement_from_dict = DtoAnnouncement.from_dict(dto_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


