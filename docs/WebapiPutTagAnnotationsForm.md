# WebapiPutTagAnnotationsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[WebapiPutTagAnnotation]**](WebapiPutTagAnnotation.md) |  | [optional] 

## Example

```python
from cnb_api.models.webapi_put_tag_annotations_form import WebapiPutTagAnnotationsForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPutTagAnnotationsForm from a JSON string
webapi_put_tag_annotations_form_instance = WebapiPutTagAnnotationsForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPutTagAnnotationsForm.to_json())

# convert the object into a dict
webapi_put_tag_annotations_form_dict = webapi_put_tag_annotations_form_instance.to_dict()
# create an instance of WebapiPutTagAnnotationsForm from a dict
webapi_put_tag_annotations_form_from_dict = WebapiPutTagAnnotationsForm.from_dict(webapi_put_tag_annotations_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


