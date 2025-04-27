# DtoWorkspaceDeleteResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 返回码，0 表示成功，1 表示失败 | [optional] 
**message** | **str** | 描述 | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_delete_result import DtoWorkspaceDeleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspaceDeleteResult from a JSON string
dto_workspace_delete_result_instance = DtoWorkspaceDeleteResult.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspaceDeleteResult.to_json())

# convert the object into a dict
dto_workspace_delete_result_dict = dto_workspace_delete_result_instance.to_dict()
# create an instance of DtoWorkspaceDeleteResult from a dict
dto_workspace_delete_result_from_dict = DtoWorkspaceDeleteResult.from_dict(dto_workspace_delete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


