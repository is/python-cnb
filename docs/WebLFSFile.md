# WebLFSFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 
**size** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_lfs_file import WebLFSFile

# TODO update the JSON string below
json = "{}"
# create an instance of WebLFSFile from a JSON string
web_lfs_file_instance = WebLFSFile.from_json(json)
# print the JSON string representation of the object
print(WebLFSFile.to_json())

# convert the object into a dict
web_lfs_file_dict = web_lfs_file_instance.to_dict()
# create an instance of WebLFSFile from a dict
web_lfs_file_from_dict = WebLFSFile.from_dict(web_lfs_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


