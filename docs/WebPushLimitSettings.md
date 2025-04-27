# WebPushLimitSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_single_push_number** | **int** |  | [optional] 
**check_single_push_number** | **bool** |  | [optional] 
**only_master_can_push_tag** | **bool** |  | [optional] 
**push_committer_must_be** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_push_limit_settings import WebPushLimitSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WebPushLimitSettings from a JSON string
web_push_limit_settings_instance = WebPushLimitSettings.from_json(json)
# print the JSON string representation of the object
print(WebPushLimitSettings.to_json())

# convert the object into a dict
web_push_limit_settings_dict = web_push_limit_settings_instance.to_dict()
# create an instance of WebPushLimitSettings from a dict
web_push_limit_settings_from_dict = WebPushLimitSettings.from_dict(web_push_limit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


