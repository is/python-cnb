# DtoOhpmTagDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**dependencies** | [**List[DtoDependency]**](DtoDependency.md) |  | [optional] 
**desc** | **str** |  | [optional] 
**files** | [**List[DtoFile]**](DtoFile.md) |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**package** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**tags** | [**List[DtoOhpmTag]**](DtoOhpmTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_ohpm_tag_detail import DtoOhpmTagDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoOhpmTagDetail from a JSON string
dto_ohpm_tag_detail_instance = DtoOhpmTagDetail.from_json(json)
# print the JSON string representation of the object
print(DtoOhpmTagDetail.to_json())

# convert the object into a dict
dto_ohpm_tag_detail_dict = dto_ohpm_tag_detail_instance.to_dict()
# create an instance of DtoOhpmTagDetail from a dict
dto_ohpm_tag_detail_from_dict = DtoOhpmTagDetail.from_dict(dto_ohpm_tag_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


