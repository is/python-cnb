# ChartMaintainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email is an optional email address to contact the named maintainer | [optional] 
**name** | **str** | Name is a user name or organization name | [optional] 
**url** | **str** | URL is an optional URL to an address for the named maintainer | [optional] 

## Example

```python
from cnb_api.models.chart_maintainer import ChartMaintainer

# TODO update the JSON string below
json = "{}"
# create an instance of ChartMaintainer from a JSON string
chart_maintainer_instance = ChartMaintainer.from_json(json)
# print the JSON string representation of the object
print(ChartMaintainer.to_json())

# convert the object into a dict
chart_maintainer_dict = chart_maintainer_instance.to_dict()
# create an instance of ChartMaintainer from a dict
chart_maintainer_from_dict = ChartMaintainer.from_dict(chart_maintainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


