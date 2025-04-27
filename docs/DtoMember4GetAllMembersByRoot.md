# DtoMember4GetAllMembersByRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**inviter** | [**DtoUsers**](DtoUsers.md) |  | [optional] 
**join_time** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**user_freeze** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 

## Example

```python
from cnb_api.models.dto_member4_get_all_members_by_root import DtoMember4GetAllMembersByRoot

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMember4GetAllMembersByRoot from a JSON string
dto_member4_get_all_members_by_root_instance = DtoMember4GetAllMembersByRoot.from_json(json)
# print the JSON string representation of the object
print(DtoMember4GetAllMembersByRoot.to_json())

# convert the object into a dict
dto_member4_get_all_members_by_root_dict = dto_member4_get_all_members_by_root_instance.to_dict()
# create an instance of DtoMember4GetAllMembersByRoot from a dict
dto_member4_get_all_members_by_root_from_dict = DtoMember4GetAllMembersByRoot.from_dict(dto_member4_get_all_members_by_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


