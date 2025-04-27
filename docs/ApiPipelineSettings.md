# ApiPipelineSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_trigger** | **bool** |  | [optional] 
**forked_repo_auto_trigger** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.api_pipeline_settings import ApiPipelineSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPipelineSettings from a JSON string
api_pipeline_settings_instance = ApiPipelineSettings.from_json(json)
# print the JSON string representation of the object
print(ApiPipelineSettings.to_json())

# convert the object into a dict
api_pipeline_settings_dict = api_pipeline_settings_instance.to_dict()
# create an instance of ApiPipelineSettings from a dict
api_pipeline_settings_from_dict = ApiPipelineSettings.from_dict(api_pipeline_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


