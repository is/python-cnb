# WebTreeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_lfs** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**submodule** | [**WebSubmodule**](WebSubmodule.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_tree_entry import WebTreeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebTreeEntry from a JSON string
web_tree_entry_instance = WebTreeEntry.from_json(json)
# print the JSON string representation of the object
print(WebTreeEntry.to_json())

# convert the object into a dict
web_tree_entry_dict = web_tree_entry_instance.to_dict()
# create an instance of WebTreeEntry from a dict
web_tree_entry_from_dict = WebTreeEntry.from_dict(web_tree_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


