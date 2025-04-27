# WebFieldInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | [**WebFieldInfoPriority**](WebFieldInfoPriority.md) |  | [optional] 
**status** | [**WebFieldInfoStatus**](WebFieldInfoStatus.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_field_info import WebFieldInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebFieldInfo from a JSON string
web_field_info_instance = WebFieldInfo.from_json(json)
# print the JSON string representation of the object
print(WebFieldInfo.to_json())

# convert the object into a dict
web_field_info_dict = web_field_info_instance.to_dict()
# create an instance of WebFieldInfo from a dict
web_field_info_from_dict = WebFieldInfo.from_dict(web_field_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


