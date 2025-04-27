# HandlerCreateLabelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_create_label_form import HandlerCreateLabelForm

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerCreateLabelForm from a JSON string
handler_create_label_form_instance = HandlerCreateLabelForm.from_json(json)
# print the JSON string representation of the object
print(HandlerCreateLabelForm.to_json())

# convert the object into a dict
handler_create_label_form_dict = handler_create_label_form_instance.to_dict()
# create an instance of HandlerCreateLabelForm from a dict
handler_create_label_form_from_dict = HandlerCreateLabelForm.from_dict(handler_create_label_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


