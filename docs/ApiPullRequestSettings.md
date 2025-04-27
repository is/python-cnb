# ApiPullRequestSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_merge_commit_merge** | **bool** |  | [optional] 
**allow_rebase_merge** | **bool** |  | [optional] 
**allow_squash_merge** | **bool** |  | [optional] 
**master_auto_as_reviewer** | **bool** |  | [optional] 
**merge_commit_message_style** | **str** |  | [optional] 
**squash_commit_message_style** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_request_settings import ApiPullRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRequestSettings from a JSON string
api_pull_request_settings_instance = ApiPullRequestSettings.from_json(json)
# print the JSON string representation of the object
print(ApiPullRequestSettings.to_json())

# convert the object into a dict
api_pull_request_settings_dict = api_pull_request_settings_instance.to_dict()
# create an instance of ApiPullRequestSettings from a dict
api_pull_request_settings_from_dict = ApiPullRequestSettings.from_dict(api_pull_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


