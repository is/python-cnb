# DtoBuildStatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipelines_status** | [**Dict[str, DtoPipelineStatus]**](DtoPipelineStatus.md) | 流水线的状态 | [optional] 
**status** | **str** | 构建状态 | [optional] 

## Example

```python
from cnb_api.models.dto_build_status_result import DtoBuildStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBuildStatusResult from a JSON string
dto_build_status_result_instance = DtoBuildStatusResult.from_json(json)
# print the JSON string representation of the object
print(DtoBuildStatusResult.to_json())

# convert the object into a dict
dto_build_status_result_dict = dto_build_status_result_instance.to_dict()
# create an instance of DtoBuildStatusResult from a dict
dto_build_status_result_from_dict = DtoBuildStatusResult.from_dict(dto_build_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


