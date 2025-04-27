# DtoWorkspaceDetailResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Cursor 客户端 remote-ssh 访问 schema 地址 | [optional] 
**vscode** | **str** | VSCode 客户端 remote-ssh 访问 schema 地址 | [optional] 
**webide** | **str** | WebIDE 访问 url | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_detail_result import DtoWorkspaceDetailResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspaceDetailResult from a JSON string
dto_workspace_detail_result_instance = DtoWorkspaceDetailResult.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspaceDetailResult.to_json())

# convert the object into a dict
dto_workspace_detail_result_dict = dto_workspace_detail_result_instance.to_dict()
# create an instance of DtoWorkspaceDetailResult from a dict
dto_workspace_detail_result_from_dict = DtoWorkspaceDetailResult.from_dict(dto_workspace_detail_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


