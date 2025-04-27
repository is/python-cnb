# DtoBuildResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_log_url** | **str** | 构建链接 | [optional] 
**message** | **str** | message | [optional] 
**sn** | **str** | 构建号 | [optional] 

## Example

```python
from cnb_api.models.dto_build_result import DtoBuildResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBuildResult from a JSON string
dto_build_result_instance = DtoBuildResult.from_json(json)
# print the JSON string representation of the object
print(DtoBuildResult.to_json())

# convert the object into a dict
dto_build_result_dict = dto_build_result_instance.to_dict()
# create an instance of DtoBuildResult from a dict
dto_build_result_from_dict = DtoBuildResult.from_dict(dto_build_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


