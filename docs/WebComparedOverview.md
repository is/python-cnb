# WebComparedOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**file_count** | **int** |  | [optional] 
**head_commit** | **str** |  | [optional] 
**merge_base_commit** | **str** |  | [optional] 
**straight** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_compared_overview import WebComparedOverview

# TODO update the JSON string below
json = "{}"
# create an instance of WebComparedOverview from a JSON string
web_compared_overview_instance = WebComparedOverview.from_json(json)
# print the JSON string representation of the object
print(WebComparedOverview.to_json())

# convert the object into a dict
web_compared_overview_dict = web_compared_overview_instance.to_dict()
# create an instance of WebComparedOverview from a dict
web_compared_overview_from_dict = WebComparedOverview.from_dict(web_compared_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


