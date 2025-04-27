# DtoPackageDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker** | [**DtoContainerPackageDetail**](DtoContainerPackageDetail.md) |  | [optional] 
**helm** | [**DtoChartPackageDetail**](DtoChartPackageDetail.md) |  | [optional] 
**maven** | [**DtoMavenPackageDetail**](DtoMavenPackageDetail.md) |  | [optional] 
**npm** | [**DtoNpmPackageDetail**](DtoNpmPackageDetail.md) |  | [optional] 
**ohpm** | [**DtoOhpmPackageDetail**](DtoOhpmPackageDetail.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_package_detail import DtoPackageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPackageDetail from a JSON string
dto_package_detail_instance = DtoPackageDetail.from_json(json)
# print the JSON string representation of the object
print(DtoPackageDetail.to_json())

# convert the object into a dict
dto_package_detail_dict = dto_package_detail_instance.to_dict()
# create an instance of DtoPackageDetail from a dict
dto_package_detail_from_dict = DtoPackageDetail.from_dict(dto_package_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


