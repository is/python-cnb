# DtoRegistryPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clean_policy_detail** | [**DtoRegistryCleanDetail**](DtoRegistryCleanDetail.md) |  | [optional] 
**overwrite_policy** | [**DtoOverwritePolicy**](DtoOverwritePolicy.md) |  | [optional] 
**version_policy** | [**DtoVersionPolicy**](DtoVersionPolicy.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_registry_policy import DtoRegistryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRegistryPolicy from a JSON string
dto_registry_policy_instance = DtoRegistryPolicy.from_json(json)
# print the JSON string representation of the object
print(DtoRegistryPolicy.to_json())

# convert the object into a dict
dto_registry_policy_dict = dto_registry_policy_instance.to_dict()
# create an instance of DtoRegistryPolicy from a dict
dto_registry_policy_from_dict = DtoRegistryPolicy.from_dict(dto_registry_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


