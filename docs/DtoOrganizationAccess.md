# DtoOrganizationAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_role** | [**ConstantAccessRole**](ConstantAccessRole.md) | AccessRole 用户在当前资源的最大权限 | [optional] 
**all_member_count** | **int** |  | [optional] 
**all_sub_group_count** | **int** | 下面所有层级子组织 | [optional] 
**all_sub_mission_count** | **int** | 下面所有层级子任务 | [optional] 
**all_sub_registry_count** | **int** |  | [optional] 
**all_sub_repo_count** | **int** | 下面所有层级子仓库 | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**follow_count** | **int** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**has_sub_group** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**member_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**remark** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**sub_group_count** | **int** | 下一级子组织数量 | [optional] 
**sub_mission_count** | **int** |  | [optional] 
**sub_registry_count** | **int** |  | [optional] 
**sub_repo_count** | **int** | 下一级子仓库 | [optional] 
**updated_at** | **str** |  | [optional] 
**wechat_mp** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_organization_access import DtoOrganizationAccess

# TODO update the JSON string below
json = "{}"
# create an instance of DtoOrganizationAccess from a JSON string
dto_organization_access_instance = DtoOrganizationAccess.from_json(json)
# print the JSON string representation of the object
print(DtoOrganizationAccess.to_json())

# convert the object into a dict
dto_organization_access_dict = dto_organization_access_instance.to_dict()
# create an instance of DtoOrganizationAccess from a dict
dto_organization_access_from_dict = DtoOrganizationAccess.from_dict(dto_organization_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


