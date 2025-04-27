# DtoLogInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_log_url** | **str** | 构建日志 url | [optional] 
**commit_title** | **str** | 提交日志 title | [optional] 
**create_time** | **str** | 构建开始时间 | [optional] 
**duration** | **int** | 构建耗时，单位：ms | [optional] 
**event** | **str** | 事件名 | [optional] 
**event_url** | **str** | 事件 url | [optional] 
**freeze** | **bool** | 构建用户是否被冻结 | [optional] 
**group_name** | **str** | 组织名 | [optional] 
**labels** | **str** | 流水线标签 | [optional] 
**nick_name** | **str** | 构建用户昵称 | [optional] 
**pipeline_fail_count** | **int** | 失败的子流水线个数 | [optional] 
**pipeline_success_count** | **int** | 成功的子流水线个数 | [optional] 
**pipeline_total_count** | **int** | 子流水线个数 | [optional] 
**sha** | **str** | commitid | [optional] 
**slug** | **str** | 仓库路径 | [optional] 
**sn** | **str** | 构建号 | [optional] 
**source_ref** | **str** | 源分支名 | [optional] 
**source_slug** | **str** | 源仓库路径 | [optional] 
**status** | **str** | 构建状态 | [optional] 
**target_ref** | **str** | 目标分支名 | [optional] 
**title** | **str** | 构建 title | [optional] 
**user_name** | **str** | 用户名 | [optional] 

## Example

```python
from cnb_api.models.dto_log_info import DtoLogInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoLogInfo from a JSON string
dto_log_info_instance = DtoLogInfo.from_json(json)
# print the JSON string representation of the object
print(DtoLogInfo.to_json())

# convert the object into a dict
dto_log_info_dict = dto_log_info_instance.to_dict()
# create an instance of DtoLogInfo from a dict
dto_log_info_from_dict = DtoLogInfo.from_dict(dto_log_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


