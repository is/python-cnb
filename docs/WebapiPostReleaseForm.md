# WebapiPostReleaseForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**is_prerelease** | **bool** |  | [optional] 
**make_latest** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_release_form import WebapiPostReleaseForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostReleaseForm from a JSON string
webapi_post_release_form_instance = WebapiPostReleaseForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostReleaseForm.to_json())

# convert the object into a dict
webapi_post_release_form_dict = webapi_post_release_form_instance.to_dict()
# create an instance of WebapiPostReleaseForm from a dict
webapi_post_release_form_from_dict = WebapiPostReleaseForm.from_dict(webapi_post_release_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


