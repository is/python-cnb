# DtoSlugs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_type** | [**ConstantSlugType**](ConstantSlugType.md) |  | [optional] 
**root_freeze** | **bool** |  | [optional] 
**root_id** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_slugs import DtoSlugs

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSlugs from a JSON string
dto_slugs_instance = DtoSlugs.from_json(json)
# print the JSON string representation of the object
print(DtoSlugs.to_json())

# convert the object into a dict
dto_slugs_dict = dto_slugs_instance.to_dict()
# create an instance of DtoSlugs from a dict
dto_slugs_from_dict = DtoSlugs.from_dict(dto_slugs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


