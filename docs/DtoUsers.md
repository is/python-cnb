# DtoUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 

## Example

```python
from cnb_api.models.dto_users import DtoUsers

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsers from a JSON string
dto_users_instance = DtoUsers.from_json(json)
# print the JSON string representation of the object
print(DtoUsers.to_json())

# convert the object into a dict
dto_users_dict = dto_users_instance.to_dict()
# create an instance of DtoUsers from a dict
dto_users_from_dict = DtoUsers.from_dict(dto_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


