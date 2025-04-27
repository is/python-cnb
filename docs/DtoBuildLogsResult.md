# DtoBuildLogsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DtoLogInfo]**](DtoLogInfo.md) | 构建数据列表 | [optional] 
**init** | **bool** | 当前仓库是否已经有构建记录，1 表示有构建记录，0 表示没有构建记录 | [optional] 
**timestamp** | **int** | 当前时间戳 | [optional] 
**total** | **int** | 总数 | [optional] 

## Example

```python
from cnb_api.models.dto_build_logs_result import DtoBuildLogsResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBuildLogsResult from a JSON string
dto_build_logs_result_instance = DtoBuildLogsResult.from_json(json)
# print the JSON string representation of the object
print(DtoBuildLogsResult.to_json())

# convert the object into a dict
dto_build_logs_result_dict = dto_build_logs_result_instance.to_dict()
# create an instance of DtoBuildLogsResult from a dict
dto_build_logs_result_from_dict = DtoBuildLogsResult.from_dict(dto_build_logs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


