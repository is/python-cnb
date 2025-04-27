# DtoGroupSettingReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_verification** | **str** | 组织限制指定邮箱认证才能加入 | [optional] 
**group_protection** | **int** | 组织保护开关，0 - 关闭，1 - 打开 | [optional] 
**hide_members** | **int** | 是否对外隐藏组织成员，0 - 否, 1 - 是 | [optional] 
**hide_sub_groups** | **int** | 是否对外隐藏子组织，0 - 否, 1 - 是 | [optional] 
**show_private_repo_watermark** | **int** | 是否对外显示私有仓库水印，0 - 否, 1 - 是 | [optional] 
**values** | **str** | SettingValue 组织设置值，多个选项，用逗号拼接。可选值来自 SettingNamesArray 的值，e.g. disable_organization_readme,cloud_native_dev_only | [optional] 

## Example

```python
from cnb_api.models.dto_group_setting_req import DtoGroupSettingReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGroupSettingReq from a JSON string
dto_group_setting_req_instance = DtoGroupSettingReq.from_json(json)
# print the JSON string representation of the object
print(DtoGroupSettingReq.to_json())

# convert the object into a dict
dto_group_setting_req_dict = dto_group_setting_req_instance.to_dict()
# create an instance of DtoGroupSettingReq from a dict
dto_group_setting_req_from_dict = DtoGroupSettingReq.from_dict(dto_group_setting_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


