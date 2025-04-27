# WebapiCreateTagForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_create_tag_form import WebapiCreateTagForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiCreateTagForm from a JSON string
webapi_create_tag_form_instance = WebapiCreateTagForm.from_json(json)
# print the JSON string representation of the object
print(WebapiCreateTagForm.to_json())

# convert the object into a dict
webapi_create_tag_form_dict = webapi_create_tag_form_instance.to_dict()
# create an instance of WebapiCreateTagForm from a dict
webapi_create_tag_form_from_dict = WebapiCreateTagForm.from_dict(webapi_create_tag_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


