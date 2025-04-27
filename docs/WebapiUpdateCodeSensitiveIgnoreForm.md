# WebapiUpdateCodeSensitiveIgnoreForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore** | **bool** |  | [optional] 
**ignore_reason** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_update_code_sensitive_ignore_form import WebapiUpdateCodeSensitiveIgnoreForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiUpdateCodeSensitiveIgnoreForm from a JSON string
webapi_update_code_sensitive_ignore_form_instance = WebapiUpdateCodeSensitiveIgnoreForm.from_json(json)
# print the JSON string representation of the object
print(WebapiUpdateCodeSensitiveIgnoreForm.to_json())

# convert the object into a dict
webapi_update_code_sensitive_ignore_form_dict = webapi_update_code_sensitive_ignore_form_instance.to_dict()
# create an instance of WebapiUpdateCodeSensitiveIgnoreForm from a dict
webapi_update_code_sensitive_ignore_form_from_dict = WebapiUpdateCodeSensitiveIgnoreForm.from_dict(webapi_update_code_sensitive_ignore_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


