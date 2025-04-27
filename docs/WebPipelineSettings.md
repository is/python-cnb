# WebPipelineSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_trigger** | **bool** |  | [optional] 
**forked_repo_auto_trigger** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_pipeline_settings import WebPipelineSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WebPipelineSettings from a JSON string
web_pipeline_settings_instance = WebPipelineSettings.from_json(json)
# print the JSON string representation of the object
print(WebPipelineSettings.to_json())

# convert the object into a dict
web_pipeline_settings_dict = web_pipeline_settings_instance.to_dict()
# create an instance of WebPipelineSettings from a dict
web_pipeline_settings_from_dict = WebPipelineSettings.from_dict(web_pipeline_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


