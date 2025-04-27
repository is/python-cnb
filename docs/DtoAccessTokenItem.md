# DtoAccessTokenItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expired_at** | **str** |  | [optional] 
**last_activity_at** | **str** |  | [optional] 
**resource_type** | [**ConstantSlugType**](ConstantSlugType.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**token_fragment** | **str** |  | [optional] 
**token_id** | **str** | id 的 string 格式，用于兼容前端 int64 支持 | [optional] 

## Example

```python
from cnb_api.models.dto_access_token_item import DtoAccessTokenItem

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAccessTokenItem from a JSON string
dto_access_token_item_instance = DtoAccessTokenItem.from_json(json)
# print the JSON string representation of the object
print(DtoAccessTokenItem.to_json())

# convert the object into a dict
dto_access_token_item_dict = dto_access_token_item_instance.to_dict()
# create an instance of DtoAccessTokenItem from a dict
dto_access_token_item_from_dict = DtoAccessTokenItem.from_dict(dto_access_token_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


