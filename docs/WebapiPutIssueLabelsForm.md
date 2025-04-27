# WebapiPutIssueLabelsForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_put_issue_labels_form import WebapiPutIssueLabelsForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPutIssueLabelsForm from a JSON string
webapi_put_issue_labels_form_instance = WebapiPutIssueLabelsForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPutIssueLabelsForm.to_json())

# convert the object into a dict
webapi_put_issue_labels_form_dict = webapi_put_issue_labels_form_instance.to_dict()
# create an instance of WebapiPutIssueLabelsForm from a dict
webapi_put_issue_labels_form_from_dict = WebapiPutIssueLabelsForm.from_dict(webapi_put_issue_labels_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


