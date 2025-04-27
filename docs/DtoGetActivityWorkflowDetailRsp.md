# DtoGetActivityWorkflowDetailRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_workflow_datas** | [**List[DtoActivityWorkflowData]**](DtoActivityWorkflowData.md) |  | [optional] 
**next_offset** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_get_activity_workflow_detail_rsp import DtoGetActivityWorkflowDetailRsp

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetActivityWorkflowDetailRsp from a JSON string
dto_get_activity_workflow_detail_rsp_instance = DtoGetActivityWorkflowDetailRsp.from_json(json)
# print the JSON string representation of the object
print(DtoGetActivityWorkflowDetailRsp.to_json())

# convert the object into a dict
dto_get_activity_workflow_detail_rsp_dict = dto_get_activity_workflow_detail_rsp_instance.to_dict()
# create an instance of DtoGetActivityWorkflowDetailRsp from a dict
dto_get_activity_workflow_detail_rsp_from_dict = DtoGetActivityWorkflowDetailRsp.from_dict(dto_get_activity_workflow_detail_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


