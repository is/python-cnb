# DtoChartPackageDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**package** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**tag_total** | **int** |  | [optional] 
**tags** | [**List[DtoChartTag]**](DtoChartTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_chart_package_detail import DtoChartPackageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoChartPackageDetail from a JSON string
dto_chart_package_detail_instance = DtoChartPackageDetail.from_json(json)
# print the JSON string representation of the object
print(DtoChartPackageDetail.to_json())

# convert the object into a dict
dto_chart_package_detail_dict = dto_chart_package_detail_instance.to_dict()
# create an instance of DtoChartPackageDetail from a dict
dto_chart_package_detail_from_dict = DtoChartPackageDetail.from_dict(dto_chart_package_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


