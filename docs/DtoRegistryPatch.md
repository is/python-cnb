# DtoRegistryPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_registry_patch import DtoRegistryPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRegistryPatch from a JSON string
dto_registry_patch_instance = DtoRegistryPatch.from_json(json)
# print the JSON string representation of the object
print(DtoRegistryPatch.to_json())

# convert the object into a dict
dto_registry_patch_dict = dto_registry_patch_instance.to_dict()
# create an instance of DtoRegistryPatch from a dict
dto_registry_patch_from_dict = DtoRegistryPatch.from_dict(dto_registry_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


