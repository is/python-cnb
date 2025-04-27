# DtoUsersResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**appreciate_status** | **int** | 用户赞赏码状态，0-无赞赏码，1-有 | [optional] 
**avatar** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**follow_count** | **int** |  | [optional] 
**follow_mission_count** | **int** |  | [optional] 
**follow_repo_count** | **int** |  | [optional] 
**follower_count** | **int** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**gender** | **int** |  | [optional] 
**group_count** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**is_following** | **bool** | 查询人是否follow了此用户 | [optional] 
**location** | **str** |  | [optional] 
**mission_count** | **int** |  | [optional] 
**nickname** | **str** |  | [optional] 
**registry_count** | **int** |  | [optional] 
**repo_count** | **int** |  | [optional] 
**reward_amount** | **int** |  | [optional] 
**reward_count** | **int** |  | [optional] 
**site** | **str** |  | [optional] 
**stars_count** | **int** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 
**wechat_mp** | **str** |  | [optional] 
**wechat_mp_qrcode** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_users_result import DtoUsersResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsersResult from a JSON string
dto_users_result_instance = DtoUsersResult.from_json(json)
# print the JSON string representation of the object
print(DtoUsersResult.to_json())

# convert the object into a dict
dto_users_result_dict = dto_users_result_instance.to_dict()
# create an instance of DtoUsersResult from a dict
dto_users_result_from_dict = DtoUsersResult.from_dict(dto_users_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


