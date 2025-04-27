# WebFieldInfos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bug** | [**WebFieldInfo**](WebFieldInfo.md) |  | [optional] 
**stories** | [**WebFieldInfo**](WebFieldInfo.md) |  | [optional] 
**task** | [**WebFieldInfo**](WebFieldInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_field_infos import WebFieldInfos

# TODO update the JSON string below
json = "{}"
# create an instance of WebFieldInfos from a JSON string
web_field_infos_instance = WebFieldInfos.from_json(json)
# print the JSON string representation of the object
print(WebFieldInfos.to_json())

# convert the object into a dict
web_field_infos_dict = web_field_infos_instance.to_dict()
# create an instance of WebFieldInfos from a dict
web_field_infos_from_dict = WebFieldInfos.from_dict(web_field_infos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


