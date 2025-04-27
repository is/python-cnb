# DtoActivityRepos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_module** | [**ConstantRepoDisplayModule**](ConstantRepoDisplayModule.md) |  | [optional] 
**fork_count** | **int** |  | [optional] 
**fork_target** | **str** |  | [optional] 
**forked_from** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**is_star** | **bool** |  | [optional] 
**language** | **str** | 仓库程序语言，预留 | [optional] 
**last_updated_at** | [**ConvertNullTime**](ConvertNullTime.md) | 最新代码更新时间 | [optional] 
**license** | **str** |  | [optional] 
**mark_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**star_count** | **int** |  | [optional] 
**status** | [**ConstantRepoStatus**](ConstantRepoStatus.md) |  | [optional] 
**topics** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_repos import DtoActivityRepos

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityRepos from a JSON string
dto_activity_repos_instance = DtoActivityRepos.from_json(json)
# print the JSON string representation of the object
print(DtoActivityRepos.to_json())

# convert the object into a dict
dto_activity_repos_dict = dto_activity_repos_instance.to_dict()
# create an instance of DtoActivityRepos from a dict
dto_activity_repos_from_dict = DtoActivityRepos.from_dict(dto_activity_repos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


