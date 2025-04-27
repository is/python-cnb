# OpenapiPutTagAnnotationsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[OpenapiPutTagAnnotation]**](OpenapiPutTagAnnotation.md) |  | [optional] 

## Example

```python
from cnb_api.models.openapi_put_tag_annotations_form import OpenapiPutTagAnnotationsForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiPutTagAnnotationsForm from a JSON string
openapi_put_tag_annotations_form_instance = OpenapiPutTagAnnotationsForm.from_json(json)
# print the JSON string representation of the object
print(OpenapiPutTagAnnotationsForm.to_json())

# convert the object into a dict
openapi_put_tag_annotations_form_dict = openapi_put_tag_annotations_form_instance.to_dict()
# create an instance of OpenapiPutTagAnnotationsForm from a dict
openapi_put_tag_annotations_form_from_dict = OpenapiPutTagAnnotationsForm.from_dict(openapi_put_tag_annotations_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


