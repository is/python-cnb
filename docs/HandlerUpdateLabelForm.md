# HandlerUpdateLabelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_update_label_form import HandlerUpdateLabelForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerUpdateLabelForm from a JSON string
handler_update_label_form_instance = HandlerUpdateLabelForm.from_json(json)
# print the JSON string representation of the object
print(HandlerUpdateLabelForm.to_json())

# convert the object into a dict
handler_update_label_form_dict = handler_update_label_form_instance.to_dict()
# create an instance of HandlerUpdateLabelForm from a dict
handler_update_label_form_from_dict = HandlerUpdateLabelForm.from_dict(handler_update_label_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


