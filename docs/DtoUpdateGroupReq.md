# DtoUpdateGroupReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**wechat_mp** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_update_group_req import DtoUpdateGroupReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateGroupReq from a JSON string
dto_update_group_req_instance = DtoUpdateGroupReq.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateGroupReq.to_json())

# convert the object into a dict
dto_update_group_req_dict = dto_update_group_req_instance.to_dict()
# create an instance of DtoUpdateGroupReq from a dict
dto_update_group_req_from_dict = DtoUpdateGroupReq.from_dict(dto_update_group_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


