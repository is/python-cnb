# OpenapiCreateBranchForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**start_point** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_create_branch_form import OpenapiCreateBranchForm

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiCreateBranchForm from a JSON string
openapi_create_branch_form_instance = OpenapiCreateBranchForm.from_json(json)
# print the JSON string representation of the object
print(OpenapiCreateBranchForm.to_json())

# convert the object into a dict
openapi_create_branch_form_dict = openapi_create_branch_form_instance.to_dict()
# create an instance of OpenapiCreateBranchForm from a dict
openapi_create_branch_form_from_dict = OpenapiCreateBranchForm.from_dict(openapi_create_branch_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


