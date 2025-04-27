# DtoMemberAccessLevelInSlugUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**inherit** | **bool** |  | [optional] 
**read_privilege** | **bool** |  | [optional] 
**write_privilege** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.dto_member_access_level_in_slug_union import DtoMemberAccessLevelInSlugUnion

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMemberAccessLevelInSlugUnion from a JSON string
dto_member_access_level_in_slug_union_instance = DtoMemberAccessLevelInSlugUnion.from_json(json)
# print the JSON string representation of the object
print(DtoMemberAccessLevelInSlugUnion.to_json())

# convert the object into a dict
dto_member_access_level_in_slug_union_dict = dto_member_access_level_in_slug_union_instance.to_dict()
# create an instance of DtoMemberAccessLevelInSlugUnion from a dict
dto_member_access_level_in_slug_union_from_dict = DtoMemberAccessLevelInSlugUnion.from_dict(dto_member_access_level_in_slug_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


