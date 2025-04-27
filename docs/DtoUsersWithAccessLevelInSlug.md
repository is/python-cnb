# DtoUsersWithAccessLevelInSlug


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verification** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**inviter** | [**DtoUsers**](DtoUsers.md) |  | [optional] 
**join_time** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 

## Example

```python
from cnb_api.models.dto_users_with_access_level_in_slug import DtoUsersWithAccessLevelInSlug

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsersWithAccessLevelInSlug from a JSON string
dto_users_with_access_level_in_slug_instance = DtoUsersWithAccessLevelInSlug.from_json(json)
# print the JSON string representation of the object
print(DtoUsersWithAccessLevelInSlug.to_json())

# convert the object into a dict
dto_users_with_access_level_in_slug_dict = dto_users_with_access_level_in_slug_instance.to_dict()
# create an instance of DtoUsersWithAccessLevelInSlug from a dict
dto_users_with_access_level_in_slug_from_dict = DtoUsersWithAccessLevelInSlug.from_dict(dto_users_with_access_level_in_slug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


