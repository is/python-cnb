# HandlerUpdateItemField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.handler_update_item_field import HandlerUpdateItemField

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerUpdateItemField from a JSON string
handler_update_item_field_instance = HandlerUpdateItemField.from_json(json)
# print the JSON string representation of the object
print(HandlerUpdateItemField.to_json())

# convert the object into a dict
handler_update_item_field_dict = handler_update_item_field_instance.to_dict()
# create an instance of HandlerUpdateItemField from a dict
handler_update_item_field_from_dict = HandlerUpdateItemField.from_dict(handler_update_item_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


