# DtoNpmTagDetail


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
**tags** | [**List[DtoNpmTag]**](DtoNpmTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_npm_tag_detail import DtoNpmTagDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoNpmTagDetail from a JSON string
dto_npm_tag_detail_instance = DtoNpmTagDetail.from_json(json)
# print the JSON string representation of the object
print(DtoNpmTagDetail.to_json())

# convert the object into a dict
dto_npm_tag_detail_dict = dto_npm_tag_detail_instance.to_dict()
# create an instance of DtoNpmTagDetail from a dict
dto_npm_tag_detail_from_dict = DtoNpmTagDetail.from_dict(dto_npm_tag_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


