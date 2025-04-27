# DtoWorkspaceListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** | 开发环境状态，running: 开发环境已启动，closed：开发环境已关闭 | [optional] 
**list** | [**List[DtoWorkspaceInfo]**](DtoWorkspaceInfo.md) | 查询开始时间，格式：YYYY-MM-DD HH:mm:ssZZ，例如：2024-12-01 00:00:00+0800 | [optional] 
**page_info** | [**DtoWorkspacePageInfo**](DtoWorkspacePageInfo.md) | 查询结束时间，格式：YYYY-MM-DD HH:mm:ssZZ，例如：2024-12-01 00:00:00+0800 | [optional] 
**total** | **int** | 分支名，例如：main | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_list_result import DtoWorkspaceListResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspaceListResult from a JSON string
dto_workspace_list_result_instance = DtoWorkspaceListResult.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspaceListResult.to_json())

# convert the object into a dict
dto_workspace_list_result_dict = dto_workspace_list_result_instance.to_dict()
# create an instance of DtoWorkspaceListResult from a dict
dto_workspace_list_result_from_dict = DtoWorkspaceListResult.from_dict(dto_workspace_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


