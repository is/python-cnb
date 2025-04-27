# WebapiPutCommitAnnotationsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[WebapiPutCommitAnnotation]**](WebapiPutCommitAnnotation.md) |  | [optional] 

## Example

```python
from cnb_api.models.webapi_put_commit_annotations_form import WebapiPutCommitAnnotationsForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPutCommitAnnotationsForm from a JSON string
webapi_put_commit_annotations_form_instance = WebapiPutCommitAnnotationsForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPutCommitAnnotationsForm.to_json())

# convert the object into a dict
webapi_put_commit_annotations_form_dict = webapi_put_commit_annotations_form_instance.to_dict()
# create an instance of WebapiPutCommitAnnotationsForm from a dict
webapi_put_commit_annotations_form_from_dict = WebapiPutCommitAnnotationsForm.from_dict(webapi_put_commit_annotations_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


