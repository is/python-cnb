# DtoGetTodoDetailRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_datas** | [**List[DtoIssueData]**](DtoIssueData.md) |  | [optional] 
**pull_request_datas** | [**List[DtoPullRequestData]**](DtoPullRequestData.md) |  | [optional] 
**todo_type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_get_todo_detail_rsp import DtoGetTodoDetailRsp

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetTodoDetailRsp from a JSON string
dto_get_todo_detail_rsp_instance = DtoGetTodoDetailRsp.from_json(json)
# print the JSON string representation of the object
print(DtoGetTodoDetailRsp.to_json())

# convert the object into a dict
dto_get_todo_detail_rsp_dict = dto_get_todo_detail_rsp_instance.to_dict()
# create an instance of DtoGetTodoDetailRsp from a dict
dto_get_todo_detail_rsp_from_dict = DtoGetTodoDetailRsp.from_dict(dto_get_todo_detail_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


