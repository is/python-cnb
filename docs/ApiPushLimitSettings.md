# ApiPushLimitSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_single_push_number** | **int** |  | [optional] 
**check_single_push_number** | **bool** |  | [optional] 
**only_master_can_push_tag** | **bool** |  | [optional] 
**push_commit_must_be** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_push_limit_settings import ApiPushLimitSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPushLimitSettings from a JSON string
api_push_limit_settings_instance = ApiPushLimitSettings.from_json(json)
# print the JSON string representation of the object
print(ApiPushLimitSettings.to_json())

# convert the object into a dict
api_push_limit_settings_dict = api_push_limit_settings_instance.to_dict()
# create an instance of ApiPushLimitSettings from a dict
api_push_limit_settings_from_dict = ApiPushLimitSettings.from_dict(api_push_limit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


