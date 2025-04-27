# DtoChartTagDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**is_deprecated** | **bool** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**metadata** | [**ChartMetadata**](ChartMetadata.md) |  | [optional] 
**package** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_chart_tag_detail import DtoChartTagDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoChartTagDetail from a JSON string
dto_chart_tag_detail_instance = DtoChartTagDetail.from_json(json)
# print the JSON string representation of the object
print(DtoChartTagDetail.to_json())

# convert the object into a dict
dto_chart_tag_detail_dict = dto_chart_tag_detail_instance.to_dict()
# create an instance of DtoChartTagDetail from a dict
dto_chart_tag_detail_from_dict = DtoChartTagDetail.from_dict(dto_chart_tag_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


