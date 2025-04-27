# DtoWorkspaceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | 分支名，例如：main | [optional] 
**commit_count** | **int** | 备份的 commit 数 | [optional] 
**create_time** | **str** | 开发环境创建时间，例如：2024-12-02T03:20:22.000Z | [optional] 
**duration** | **int** | 开发环境持续时间，单位：ms（非实时更新） | [optional] 
**file_count** | **int** | 备份的文件数 | [optional] 
**file_list** | **str** | 备份的文件列表，仅前五个备份文件相对路径 | [optional] 
**latest_sha** | **str** | 环境销毁时远程最新的 commit short hash | [optional] 
**pipeline_id** | **str** | 创建环境的子流水线 id | [optional] 
**remote_stash_count** | **int** | 备份的 stash 数 | [optional] 
**repo_url** | **str** | 仓库地址 | [optional] 
**restore_id** | **str** | 恢复备份代码的流水线 id，如果有值表示备份代码已被恢复（重建环境时会恢复备份代码） | [optional] 
**slug** | **str** | 仓库路径，例如：groupname/reponame | [optional] 
**sn** | **str** | 创建开发环境的流水线 sn | [optional] 
**ssh** | **bool** | 开发环境是否支持 ssh 链接 | [optional] 
**status** | **str** | 工作区状态，running: 开发环境已启动，closed：开发环境已关闭 | [optional] 
**workspace** | **str** | 开发环境默认工作区路径 | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_info import DtoWorkspaceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspaceInfo from a JSON string
dto_workspace_info_instance = DtoWorkspaceInfo.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspaceInfo.to_json())

# convert the object into a dict
dto_workspace_info_dict = dto_workspace_info_instance.to_dict()
# create an instance of DtoWorkspaceInfo from a dict
dto_workspace_info_from_dict = DtoWorkspaceInfo.from_dict(dto_workspace_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


