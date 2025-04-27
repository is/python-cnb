# DtoOutsideCollaboratorInRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**join_time** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**type** | [**ConstantUserType**](ConstantUserType.md) |  | [optional] 
**username** | **str** |  | [optional] 
**verified** | **int** | 认证类型 | [optional] 
**verified_expire_in** | **str** | 认证过期时间 | [optional] 

## Example

```python
from cnb_api.models.dto_outside_collaborator_in_repo import DtoOutsideCollaboratorInRepo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoOutsideCollaboratorInRepo from a JSON string
dto_outside_collaborator_in_repo_instance = DtoOutsideCollaboratorInRepo.from_json(json)
# print the JSON string representation of the object
print(DtoOutsideCollaboratorInRepo.to_json())

# convert the object into a dict
dto_outside_collaborator_in_repo_dict = dto_outside_collaborator_in_repo_instance.to_dict()
# create an instance of DtoOutsideCollaboratorInRepo from a dict
dto_outside_collaborator_in_repo_from_dict = DtoOutsideCollaboratorInRepo.from_dict(dto_outside_collaborator_in_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


