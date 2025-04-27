# WebPreloadFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**file_stat** | [**WebFileStat**](WebFileStat.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_preload_file import WebPreloadFile

# TODO update the JSON string below
json = "{}"
# create an instance of WebPreloadFile from a JSON string
web_preload_file_instance = WebPreloadFile.from_json(json)
# print the JSON string representation of the object
print(WebPreloadFile.to_json())

# convert the object into a dict
web_preload_file_dict = web_preload_file_instance.to_dict()
# create an instance of WebPreloadFile from a dict
web_preload_file_from_dict = WebPreloadFile.from_dict(web_preload_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


