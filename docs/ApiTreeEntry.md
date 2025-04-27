# ApiTreeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_tree_entry import ApiTreeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTreeEntry from a JSON string
api_tree_entry_instance = ApiTreeEntry.from_json(json)
# print the JSON string representation of the object
print(ApiTreeEntry.to_json())

# convert the object into a dict
api_tree_entry_dict = api_tree_entry_instance.to_dict()
# create an instance of ApiTreeEntry from a dict
api_tree_entry_from_dict = ApiTreeEntry.from_dict(api_tree_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


