# WebDiffEntry


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

## Example

```python
from cnb_api.models.web_diff_entry import WebDiffEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiffEntry from a JSON string
web_diff_entry_instance = WebDiffEntry.from_json(json)
# print the JSON string representation of the object
print(WebDiffEntry.to_json())

# convert the object into a dict
web_diff_entry_dict = web_diff_entry_instance.to_dict()
# create an instance of WebDiffEntry from a dict
web_diff_entry_from_dict = WebDiffEntry.from_dict(web_diff_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


