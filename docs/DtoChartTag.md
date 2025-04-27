# DtoChartTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**digest** | **str** |  | [optional] 
**is_deprecated** | **bool** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**metadata** | [**ChartMetadata**](ChartMetadata.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_chart_tag import DtoChartTag

# TODO update the JSON string below
json = "{}"
# create an instance of DtoChartTag from a JSON string
dto_chart_tag_instance = DtoChartTag.from_json(json)
# print the JSON string representation of the object
print(DtoChartTag.to_json())

# convert the object into a dict
dto_chart_tag_dict = dto_chart_tag_instance.to_dict()
# create an instance of DtoChartTag from a dict
dto_chart_tag_from_dict = DtoChartTag.from_dict(dto_chart_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


