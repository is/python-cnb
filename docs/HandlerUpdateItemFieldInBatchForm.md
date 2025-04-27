# HandlerUpdateItemFieldInBatchForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_item_fields** | [**List[HandlerUpdateItemField]**](HandlerUpdateItemField.md) |  | [optional] 

## Example

```python
from cnb_api.models.handler_update_item_field_in_batch_form import HandlerUpdateItemFieldInBatchForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerUpdateItemFieldInBatchForm from a JSON string
handler_update_item_field_in_batch_form_instance = HandlerUpdateItemFieldInBatchForm.from_json(json)
# print the JSON string representation of the object
print(HandlerUpdateItemFieldInBatchForm.to_json())

# convert the object into a dict
handler_update_item_field_in_batch_form_dict = handler_update_item_field_in_batch_form_instance.to_dict()
# create an instance of HandlerUpdateItemFieldInBatchForm from a dict
handler_update_item_field_in_batch_form_from_dict = HandlerUpdateItemFieldInBatchForm.from_dict(handler_update_item_field_in_batch_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


