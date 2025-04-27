# WebComparedFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**diff** | [**WebDiff**](WebDiff.md) |  | [optional] 
**head_commit** | **str** |  | [optional] 
**merge_base_commit** | **str** |  | [optional] 
**straight** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_compared_files import WebComparedFiles

# TODO update the JSON string below
json = "{}"
# create an instance of WebComparedFiles from a JSON string
web_compared_files_instance = WebComparedFiles.from_json(json)
# print the JSON string representation of the object
print(WebComparedFiles.to_json())

# convert the object into a dict
web_compared_files_dict = web_compared_files_instance.to_dict()
# create an instance of WebComparedFiles from a dict
web_compared_files_from_dict = WebComparedFiles.from_dict(web_compared_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


