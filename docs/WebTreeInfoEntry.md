# WebTreeInfoEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_tree_info_entry import WebTreeInfoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebTreeInfoEntry from a JSON string
web_tree_info_entry_instance = WebTreeInfoEntry.from_json(json)
# print the JSON string representation of the object
print(WebTreeInfoEntry.to_json())

# convert the object into a dict
web_tree_info_entry_dict = web_tree_info_entry_instance.to_dict()
# create an instance of WebTreeInfoEntry from a dict
web_tree_info_entry_from_dict = WebTreeInfoEntry.from_dict(web_tree_info_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


