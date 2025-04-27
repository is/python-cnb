# ScopeRawItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.scope_raw_item import ScopeRawItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeRawItem from a JSON string
scope_raw_item_instance = ScopeRawItem.from_json(json)
# print the JSON string representation of the object
print(ScopeRawItem.to_json())

# convert the object into a dict
scope_raw_item_dict = scope_raw_item_instance.to_dict()
# create an instance of ScopeRawItem from a dict
scope_raw_item_from_dict = ScopeRawItem.from_dict(scope_raw_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


