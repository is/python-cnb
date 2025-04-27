# DtoUserFollowResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freeze** | **bool** |  | [optional] 
**is_following** | **bool** | 查询人是否follow了此用户 | [optional] 
**nickname** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_user_follow_result import DtoUserFollowResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserFollowResult from a JSON string
dto_user_follow_result_instance = DtoUserFollowResult.from_json(json)
# print the JSON string representation of the object
print(DtoUserFollowResult.to_json())

# convert the object into a dict
dto_user_follow_result_dict = dto_user_follow_result_instance.to_dict()
# create an instance of DtoUserFollowResult from a dict
dto_user_follow_result_from_dict = DtoUserFollowResult.from_dict(dto_user_follow_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


