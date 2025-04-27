# WebapiInitRepositoryForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gitignore_template** | **str** |  | [optional] 
**is_auto_readme** | **bool** |  | [optional] 
**license_template** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_init_repository_form import WebapiInitRepositoryForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiInitRepositoryForm from a JSON string
webapi_init_repository_form_instance = WebapiInitRepositoryForm.from_json(json)
# print the JSON string representation of the object
print(WebapiInitRepositoryForm.to_json())

# convert the object into a dict
webapi_init_repository_form_dict = webapi_init_repository_form_instance.to_dict()
# create an instance of WebapiInitRepositoryForm from a dict
webapi_init_repository_form_from_dict = WebapiInitRepositoryForm.from_dict(webapi_init_repository_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


