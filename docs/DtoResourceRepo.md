# DtoResourceRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**status** | [**ConstantRepoStatus**](ConstantRepoStatus.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_resource_repo import DtoResourceRepo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResourceRepo from a JSON string
dto_resource_repo_instance = DtoResourceRepo.from_json(json)
# print the JSON string representation of the object
print(DtoResourceRepo.to_json())

# convert the object into a dict
dto_resource_repo_dict = dto_resource_repo_instance.to_dict()
# create an instance of DtoResourceRepo from a dict
dto_resource_repo_from_dict = DtoResourceRepo.from_dict(dto_resource_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


