# DtoMissionWithRepos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**repos** | [**List[DtoRepos4User]**](DtoRepos4User.md) |  | [optional] 
**stared** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_mission_with_repos import DtoMissionWithRepos

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMissionWithRepos from a JSON string
dto_mission_with_repos_instance = DtoMissionWithRepos.from_json(json)
# print the JSON string representation of the object
print(DtoMissionWithRepos.to_json())

# convert the object into a dict
dto_mission_with_repos_dict = dto_mission_with_repos_instance.to_dict()
# create an instance of DtoMissionWithRepos from a dict
dto_mission_with_repos_from_dict = DtoMissionWithRepos.from_dict(dto_mission_with_repos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


