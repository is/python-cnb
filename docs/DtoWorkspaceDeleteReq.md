# DtoWorkspaceDeleteReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_id** | **str** | 创建环境的流水线 id | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_delete_req import DtoWorkspaceDeleteReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspaceDeleteReq from a JSON string
dto_workspace_delete_req_instance = DtoWorkspaceDeleteReq.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspaceDeleteReq.to_json())

# convert the object into a dict
dto_workspace_delete_req_dict = dto_workspace_delete_req_instance.to_dict()
# create an instance of DtoWorkspaceDeleteReq from a dict
dto_workspace_delete_req_from_dict = DtoWorkspaceDeleteReq.from_dict(dto_workspace_delete_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


