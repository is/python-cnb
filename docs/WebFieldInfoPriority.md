# WebFieldInfoPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color_options** | [**List[WebFieldInfoPriorityColorOption]**](WebFieldInfoPriorityColorOption.md) |  | [optional] 
**html_type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_field_info_priority import WebFieldInfoPriority

# TODO update the JSON string below
json = "{}"
# create an instance of WebFieldInfoPriority from a JSON string
web_field_info_priority_instance = WebFieldInfoPriority.from_json(json)
# print the JSON string representation of the object
print(WebFieldInfoPriority.to_json())

# convert the object into a dict
web_field_info_priority_dict = web_field_info_priority_instance.to_dict()
# create an instance of WebFieldInfoPriority from a dict
web_field_info_priority_from_dict = WebFieldInfoPriority.from_dict(web_field_info_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


