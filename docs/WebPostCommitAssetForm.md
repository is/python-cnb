# WebPostCommitAssetForm


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
from cnb_api.models.web_post_commit_asset_form import WebPostCommitAssetForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebPostCommitAssetForm from a JSON string
web_post_commit_asset_form_instance = WebPostCommitAssetForm.from_json(json)
# print the JSON string representation of the object
print(WebPostCommitAssetForm.to_json())

# convert the object into a dict
web_post_commit_asset_form_dict = web_post_commit_asset_form_instance.to_dict()
# create an instance of WebPostCommitAssetForm from a dict
web_post_commit_asset_form_from_dict = WebPostCommitAssetForm.from_dict(web_post_commit_asset_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


