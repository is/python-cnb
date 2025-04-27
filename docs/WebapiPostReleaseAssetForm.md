# WebapiPostReleaseAssetForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size_in_byte** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_release_asset_form import WebapiPostReleaseAssetForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostReleaseAssetForm from a JSON string
webapi_post_release_asset_form_instance = WebapiPostReleaseAssetForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostReleaseAssetForm.to_json())

# convert the object into a dict
webapi_post_release_asset_form_dict = webapi_post_release_asset_form_instance.to_dict()
# create an instance of WebapiPostReleaseAssetForm from a dict
webapi_post_release_asset_form_from_dict = WebapiPostReleaseAssetForm.from_dict(webapi_post_release_asset_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


