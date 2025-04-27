# WebapiPutPullRequestLabelsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_put_pull_request_labels_form import WebapiPutPullRequestLabelsForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPutPullRequestLabelsForm from a JSON string
webapi_put_pull_request_labels_form_instance = WebapiPutPullRequestLabelsForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPutPullRequestLabelsForm.to_json())

# convert the object into a dict
webapi_put_pull_request_labels_form_dict = webapi_put_pull_request_labels_form_instance.to_dict()
# create an instance of WebapiPutPullRequestLabelsForm from a dict
webapi_put_pull_request_labels_form_from_dict = WebapiPutPullRequestLabelsForm.from_dict(webapi_put_pull_request_labels_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


