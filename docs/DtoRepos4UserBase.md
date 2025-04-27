# DtoRepos4UserBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_module** | [**ConstantRepoDisplayModule**](ConstantRepoDisplayModule.md) |  | [optional] 
**fork_count** | **int** |  | [optional] 
**forked_from_repo** | [**DtoSlugs**](DtoSlugs.md) | 预留 | [optional] 
**freeze** | **bool** |  | [optional] [readonly] 
**id** | **int** |  | [optional] 
**language** | **str** | 仓库程序语言，预留 | [optional] 
**languages** | [**DtoRepoLanguage**](DtoRepoLanguage.md) | 仓库语言 | [optional] 
**last_update_nickname** | **str** | 最新代码更新人姓名 | [optional] 
**last_update_username** | **str** | 最新代码更新人账户名 | [optional] 
**last_updated_at** | [**ConvertNullTime**](ConvertNullTime.md) | 最新代码更新时间 | [optional] 
**license** | **str** |  | [optional] 
**mark_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**open_issue_count** | **int** | 开启的issue数 | [optional] 
**open_pull_request_count** | **int** | 开启的pull request数 | [optional] 
**path** | **str** | 完整仓库路径 | [optional] 
**site** | **str** |  | [optional] 
**star_count** | **int** |  | [optional] 
**status** | [**ConstantRepoStatus**](ConstantRepoStatus.md) |  | [optional] 
**tags** | [**List[DtoRankDetailTagsInner]**](DtoRankDetailTagsInner.md) |  | [optional] 
**topics** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepos4UserBase from a JSON string
dto_repos4_user_base_instance = DtoRepos4UserBase.from_json(json)
# print the JSON string representation of the object
print(DtoRepos4UserBase.to_json())

# convert the object into a dict
dto_repos4_user_base_dict = dto_repos4_user_base_instance.to_dict()
# create an instance of DtoRepos4UserBase from a dict
dto_repos4_user_base_from_dict = DtoRepos4UserBase.from_dict(dto_repos4_user_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


