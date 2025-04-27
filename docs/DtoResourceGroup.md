# DtoResourceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**wechat_mp** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_resource_group import DtoResourceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResourceGroup from a JSON string
dto_resource_group_instance = DtoResourceGroup.from_json(json)
# print the JSON string representation of the object
print(DtoResourceGroup.to_json())

# convert the object into a dict
dto_resource_group_dict = dto_resource_group_instance.to_dict()
# create an instance of DtoResourceGroup from a dict
dto_resource_group_from_dict = DtoResourceGroup.from_dict(dto_resource_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


