# DtoTagDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker** | [**DtoContainerTagDetail**](DtoContainerTagDetail.md) |  | [optional] 
**helm** | [**DtoChartTagDetail**](DtoChartTagDetail.md) |  | [optional] 
**maven** | [**DtoMavenTagDetail**](DtoMavenTagDetail.md) |  | [optional] 
**npm** | [**DtoNpmTagDetail**](DtoNpmTagDetail.md) |  | [optional] 
**ohpm** | [**DtoOhpmTagDetail**](DtoOhpmTagDetail.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_tag_detail import DtoTagDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTagDetail from a JSON string
dto_tag_detail_instance = DtoTagDetail.from_json(json)
# print the JSON string representation of the object
print(DtoTagDetail.to_json())

# convert the object into a dict
dto_tag_detail_dict = dto_tag_detail_instance.to_dict()
# create an instance of DtoTagDetail from a dict
dto_tag_detail_from_dict = DtoTagDetail.from_dict(dto_tag_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


