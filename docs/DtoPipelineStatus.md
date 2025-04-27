# DtoPipelineStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | 流水线耗时 | [optional] 
**stages** | [**List[DtoStage]**](DtoStage.md) | 流水线各 stage 的状态 | [optional] 
**status** | **str** | 流水线状态 | [optional] 

## Example

```python
from cnb_api.models.dto_pipeline_status import DtoPipelineStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPipelineStatus from a JSON string
dto_pipeline_status_instance = DtoPipelineStatus.from_json(json)
# print the JSON string representation of the object
print(DtoPipelineStatus.to_json())

# convert the object into a dict
dto_pipeline_status_dict = dto_pipeline_status_instance.to_dict()
# create an instance of DtoPipelineStatus from a dict
dto_pipeline_status_from_dict = DtoPipelineStatus.from_dict(dto_pipeline_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


