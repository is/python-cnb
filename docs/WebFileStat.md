# WebFileStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | [**WebMIMEType**](WebMIMEType.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_file_stat import WebFileStat

# TODO update the JSON string below
json = "{}"
# create an instance of WebFileStat from a JSON string
web_file_stat_instance = WebFileStat.from_json(json)
# print the JSON string representation of the object
print(WebFileStat.to_json())

# convert the object into a dict
web_file_stat_dict = web_file_stat_instance.to_dict()
# create an instance of WebFileStat from a dict
web_file_stat_from_dict = WebFileStat.from_dict(web_file_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


