# ApiPullCreationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**head** | **str** |  | [optional] 
**head_repo** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_creation_form import ApiPullCreationForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullCreationForm from a JSON string
api_pull_creation_form_instance = ApiPullCreationForm.from_json(json)
# print the JSON string representation of the object
print(ApiPullCreationForm.to_json())

# convert the object into a dict
api_pull_creation_form_dict = api_pull_creation_form_instance.to_dict()
# create an instance of ApiPullCreationForm from a dict
api_pull_creation_form_from_dict = ApiPullCreationForm.from_dict(api_pull_creation_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


