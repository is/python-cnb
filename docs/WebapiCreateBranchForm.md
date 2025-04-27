# WebapiCreateBranchForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_branch_name** | **str** |  | [optional] 
**start_point** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_create_branch_form import WebapiCreateBranchForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiCreateBranchForm from a JSON string
webapi_create_branch_form_instance = WebapiCreateBranchForm.from_json(json)
# print the JSON string representation of the object
print(WebapiCreateBranchForm.to_json())

# convert the object into a dict
webapi_create_branch_form_dict = webapi_create_branch_form_instance.to_dict()
# create an instance of WebapiCreateBranchForm from a dict
webapi_create_branch_form_from_dict = WebapiCreateBranchForm.from_dict(webapi_create_branch_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


