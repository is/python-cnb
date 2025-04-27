# ApiPostPullLabelsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.api_post_pull_labels_form import ApiPostPullLabelsForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostPullLabelsForm from a JSON string
api_post_pull_labels_form_instance = ApiPostPullLabelsForm.from_json(json)
# print the JSON string representation of the object
print(ApiPostPullLabelsForm.to_json())

# convert the object into a dict
api_post_pull_labels_form_dict = api_post_pull_labels_form_instance.to_dict()
# create an instance of ApiPostPullLabelsForm from a dict
api_post_pull_labels_form_from_dict = ApiPostPullLabelsForm.from_dict(api_post_pull_labels_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


