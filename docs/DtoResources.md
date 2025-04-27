# DtoResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**DtoResourceGroup**](DtoResourceGroup.md) |  | [optional] 
**mission** | [**DtoResourceMission**](DtoResourceMission.md) |  | [optional] 
**registry** | [**DtoResourceRegistry**](DtoResourceRegistry.md) |  | [optional] 
**repo** | [**DtoResourceRepo**](DtoResourceRepo.md) |  | [optional] 
**type** | [**ConstantSlugType**](ConstantSlugType.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_resources import DtoResources

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResources from a JSON string
dto_resources_instance = DtoResources.from_json(json)
# print the JSON string representation of the object
print(DtoResources.to_json())

# convert the object into a dict
dto_resources_dict = dto_resources_instance.to_dict()
# create an instance of DtoResources from a dict
dto_resources_from_dict = DtoResources.from_dict(dto_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


