# DtoUpdateGroupAvatarReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | 新头像 url | [optional] 

## Example

```python
from cnb_api.models.dto_update_group_avatar_req import DtoUpdateGroupAvatarReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateGroupAvatarReq from a JSON string
dto_update_group_avatar_req_instance = DtoUpdateGroupAvatarReq.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateGroupAvatarReq.to_json())

# convert the object into a dict
dto_update_group_avatar_req_dict = dto_update_group_avatar_req_instance.to_dict()
# create an instance of DtoUpdateGroupAvatarReq from a dict
dto_update_group_avatar_req_from_dict = DtoUpdateGroupAvatarReq.from_dict(dto_update_group_avatar_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


