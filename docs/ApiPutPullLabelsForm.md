# ApiPutPullLabelsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.api_put_pull_labels_form import ApiPutPullLabelsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPutPullLabelsForm from a JSON string
api_put_pull_labels_form_instance = ApiPutPullLabelsForm.from_json(json)
# print the JSON string representation of the object
print(ApiPutPullLabelsForm.to_json())

# convert the object into a dict
api_put_pull_labels_form_dict = api_put_pull_labels_form_instance.to_dict()
# create an instance of ApiPutPullLabelsForm from a dict
api_put_pull_labels_form_from_dict = ApiPutPullLabelsForm.from_dict(api_put_pull_labels_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


