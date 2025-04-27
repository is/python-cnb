# ScopeAccessTokenConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[ScopeGroupItem]**](ScopeGroupItem.md) |  | [optional] 
**scene** | [**List[ScopeScene]**](ScopeScene.md) |  | [optional] 

## Example

```python
from cnb_api.models.scope_access_token_config import ScopeAccessTokenConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeAccessTokenConfig from a JSON string
scope_access_token_config_instance = ScopeAccessTokenConfig.from_json(json)
# print the JSON string representation of the object
print(ScopeAccessTokenConfig.to_json())

# convert the object into a dict
scope_access_token_config_dict = scope_access_token_config_instance.to_dict()
# create an instance of ScopeAccessTokenConfig from a dict
scope_access_token_config_from_dict = ScopeAccessTokenConfig.from_dict(scope_access_token_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


