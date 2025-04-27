# DtoOrganizationSettingWithParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_show_members** | **bool** | 上级group设置了hide_members为1，则下级都不能显示 | [optional] 
**can_show_sub_groups** | **bool** | 上级group设置了hide_sub_groups为1，则下级都不能显示 | [optional] 
**can_show_watermark** | **bool** |  | [optional] 
**email_verification** | **str** |  | [optional] 
**group_protection** | **int** |  | [optional] 
**hide_members** | **int** | 是否对外隐藏组织成员，0 - 否, 1 - 是 | [optional] 
**hide_sub_groups** | **int** | 是否对外隐藏子组织，0 - 否, 1 - 是 | [optional] 
**root_email_verification** | **str** |  | [optional] 
**root_group_protection** | **bool** |  | [optional] 
**root_values** | [**OrganizationSettingValue**](OrganizationSettingValue.md) |  | [optional] 
**show_private_repo_watermark** | **int** |  | [optional] 
**values** | [**OrganizationSettingValue**](OrganizationSettingValue.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_organization_setting_with_parent import DtoOrganizationSettingWithParent

# TODO update the JSON string below
json = "{}"
# create an instance of DtoOrganizationSettingWithParent from a JSON string
dto_organization_setting_with_parent_instance = DtoOrganizationSettingWithParent.from_json(json)
# print the JSON string representation of the object
print(DtoOrganizationSettingWithParent.to_json())

# convert the object into a dict
dto_organization_setting_with_parent_dict = dto_organization_setting_with_parent_instance.to_dict()
# create an instance of DtoOrganizationSettingWithParent from a dict
dto_organization_setting_with_parent_from_dict = DtoOrganizationSettingWithParent.from_dict(dto_organization_setting_with_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


