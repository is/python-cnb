# ApiPatchLabelForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The hexadecimal color code for the label, without the leading &#x60;#&#x60;. | [optional] 
**description** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_patch_label_form import ApiPatchLabelForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPatchLabelForm from a JSON string
api_patch_label_form_instance = ApiPatchLabelForm.from_json(json)
# print the JSON string representation of the object
print(ApiPatchLabelForm.to_json())

# convert the object into a dict
api_patch_label_form_dict = api_patch_label_form_instance.to_dict()
# create an instance of ApiPatchLabelForm from a dict
api_patch_label_form_from_dict = ApiPatchLabelForm.from_dict(api_patch_label_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


