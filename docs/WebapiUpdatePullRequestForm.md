# WebapiUpdatePullRequestForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_update_pull_request_form import WebapiUpdatePullRequestForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiUpdatePullRequestForm from a JSON string
webapi_update_pull_request_form_instance = WebapiUpdatePullRequestForm.from_json(json)
# print the JSON string representation of the object
print(WebapiUpdatePullRequestForm.to_json())

# convert the object into a dict
webapi_update_pull_request_form_dict = webapi_update_pull_request_form_instance.to_dict()
# create an instance of WebapiUpdatePullRequestForm from a dict
webapi_update_pull_request_form_from_dict = WebapiUpdatePullRequestForm.from_dict(webapi_update_pull_request_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


