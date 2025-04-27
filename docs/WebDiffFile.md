# WebDiffFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_type** | **str** |  | [optional] 
**deletions** | **int** |  | [optional] 
**file_index** | **int** |  | [optional] 
**insertions** | **int** |  | [optional] 
**is_bin** | **bool** |  | [optional] 
**old_path** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sections** | [**List[WebDiffSection]**](WebDiffSection.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_diff_file import WebDiffFile

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiffFile from a JSON string
web_diff_file_instance = WebDiffFile.from_json(json)
# print the JSON string representation of the object
print(WebDiffFile.to_json())

# convert the object into a dict
web_diff_file_dict = web_diff_file_instance.to_dict()
# create an instance of WebDiffFile from a dict
web_diff_file_from_dict = WebDiffFile.from_dict(web_diff_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


