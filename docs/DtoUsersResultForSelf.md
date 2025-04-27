# DtoUsersResultForSelf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**appreciate_status** | **int** | 用户赞赏码状态，0-无赞赏码，1-有 | [optional] 
**avatar** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**editable** | [**ConstantUserEditable**](ConstantUserEditable.md) |  | [optional] 
**email** | **str** |  | [optional] 
**follow_count** | **int** |  | [optional] 
**follow_mission_count** | **int** |  | [optional] 
**follow_repo_count** | **int** |  | [optional] 
**follower_count** | **int** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**gender** | **int** |  | [optional] 
**group_count** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**last_login_at** | **str** |  | [optional] 
**last_login_ip** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**mission_count** | **int** |  | [optional] 
**next_updated_name_at** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**registry_count** | **int** |  | [optional] 
**repo_count** | **int** |  | [optional] 
**reward_amount** | **int** |  | [optional] 
**reward_count** | **int** |  | [optional] 
**site** | **str** |  | [optional] 
**stars_count** | **int** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**updated_name_at** | **str** |  | [optional] 
**updated_nick_at** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 
**wechat_mp** | **str** |  | [optional] 
**wechat_mp_qrcode** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_users_result_for_self import DtoUsersResultForSelf

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsersResultForSelf from a JSON string
dto_users_result_for_self_instance = DtoUsersResultForSelf.from_json(json)
# print the JSON string representation of the object
print(DtoUsersResultForSelf.to_json())

# convert the object into a dict
dto_users_result_for_self_dict = dto_users_result_for_self_instance.to_dict()
# create an instance of DtoUsersResultForSelf from a dict
dto_users_result_for_self_from_dict = DtoUsersResultForSelf.from_dict(dto_users_result_for_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


