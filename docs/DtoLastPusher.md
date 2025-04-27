# DtoLastPusher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_frozen** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**push_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_last_pusher import DtoLastPusher

# TODO update the JSON string below
json = "{}"
# create an instance of DtoLastPusher from a JSON string
dto_last_pusher_instance = DtoLastPusher.from_json(json)
# print the JSON string representation of the object
print(DtoLastPusher.to_json())

# convert the object into a dict
dto_last_pusher_dict = dto_last_pusher_instance.to_dict()
# create an instance of DtoLastPusher from a dict
dto_last_pusher_from_dict = DtoLastPusher.from_dict(dto_last_pusher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


