# DtoTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker** | [**List[DtoContainerTag]**](DtoContainerTag.md) |  | [optional] 
**helm** | [**List[DtoChartTag]**](DtoChartTag.md) |  | [optional] 
**maven** | [**List[DtoMavenTag]**](DtoMavenTag.md) |  | [optional] 
**npm** | [**List[DtoNpmTag]**](DtoNpmTag.md) |  | [optional] 
**ohpm** | [**List[DtoOhpmTag]**](DtoOhpmTag.md) |  | [optional] 
**package** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_tag import DtoTag

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTag from a JSON string
dto_tag_instance = DtoTag.from_json(json)
# print the JSON string representation of the object
print(DtoTag.to_json())

# convert the object into a dict
dto_tag_dict = dto_tag_instance.to_dict()
# create an instance of DtoTag from a dict
dto_tag_from_dict = DtoTag.from_dict(dto_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


