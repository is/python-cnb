# DtoManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DtoManifestMetadata**](DtoManifestMetadata.md) |  | [optional] 
**type** | **str** | Type manifest/manifest_list | [optional] 

## Example

```python
from cnb_api.models.dto_manifest import DtoManifest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoManifest from a JSON string
dto_manifest_instance = DtoManifest.from_json(json)
# print the JSON string representation of the object
print(DtoManifest.to_json())

# convert the object into a dict
dto_manifest_dict = dto_manifest_instance.to_dict()
# create an instance of DtoManifest from a dict
dto_manifest_from_dict = DtoManifest.from_dict(dto_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


