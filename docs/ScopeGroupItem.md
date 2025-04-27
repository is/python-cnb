# ScopeGroupItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | [**List[ScopeRawItem]**](ScopeRawItem.md) |  | [optional] 
**group** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.scope_group_item import ScopeGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeGroupItem from a JSON string
scope_group_item_instance = ScopeGroupItem.from_json(json)
# print the JSON string representation of the object
print(ScopeGroupItem.to_json())

# convert the object into a dict
scope_group_item_dict = scope_group_item_instance.to_dict()
# create an instance of ScopeGroupItem from a dict
scope_group_item_from_dict = ScopeGroupItem.from_dict(scope_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


