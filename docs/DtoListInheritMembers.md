# DtoListInheritMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherit_path** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**users** | [**List[DtoInheritMembersUser]**](DtoInheritMembersUser.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_list_inherit_members import DtoListInheritMembers

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListInheritMembers from a JSON string
dto_list_inherit_members_instance = DtoListInheritMembers.from_json(json)
# print the JSON string representation of the object
print(DtoListInheritMembers.to_json())

# convert the object into a dict
dto_list_inherit_members_dict = dto_list_inherit_members_instance.to_dict()
# create an instance of DtoListInheritMembers from a dict
dto_list_inherit_members_from_dict = DtoListInheritMembers.from_dict(dto_list_inherit_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


