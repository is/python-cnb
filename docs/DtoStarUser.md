# DtoStarUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_follow** | **bool** |  | [optional] 
**nickname** | **str** |  | [optional] 
**stared_at** | **str** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 

## Example

```python
from cnb_api.models.dto_star_user import DtoStarUser

# TODO update the JSON string below
json = "{}"
# create an instance of DtoStarUser from a JSON string
dto_star_user_instance = DtoStarUser.from_json(json)
# print the JSON string representation of the object
print(DtoStarUser.to_json())

# convert the object into a dict
dto_star_user_dict = dto_star_user_instance.to_dict()
# create an instance of DtoStarUser from a dict
dto_star_user_from_dict = DtoStarUser.from_dict(dto_star_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


