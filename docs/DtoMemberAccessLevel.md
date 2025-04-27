# DtoMemberAccessLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_member_access_level import DtoMemberAccessLevel

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMemberAccessLevel from a JSON string
dto_member_access_level_instance = DtoMemberAccessLevel.from_json(json)
# print the JSON string representation of the object
print(DtoMemberAccessLevel.to_json())

# convert the object into a dict
dto_member_access_level_dict = dto_member_access_level_instance.to_dict()
# create an instance of DtoMemberAccessLevel from a dict
dto_member_access_level_from_dict = DtoMemberAccessLevel.from_dict(dto_member_access_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


