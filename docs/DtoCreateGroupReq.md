# DtoCreateGroupReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bind_domain** | **str** | BindDomain 根组织绑定的域名 | [optional] 
**description** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_create_group_req import DtoCreateGroupReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateGroupReq from a JSON string
dto_create_group_req_instance = DtoCreateGroupReq.from_json(json)
# print the JSON string representation of the object
print(DtoCreateGroupReq.to_json())

# convert the object into a dict
dto_create_group_req_dict = dto_create_group_req_instance.to_dict()
# create an instance of DtoCreateGroupReq from a dict
dto_create_group_req_from_dict = DtoCreateGroupReq.from_dict(dto_create_group_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


