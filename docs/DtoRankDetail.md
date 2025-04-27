# DtoRankDetail


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
**rank_value** | **int** |  | [optional] 
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
from cnb_api.models.dto_rank_detail import DtoRankDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRankDetail from a JSON string
dto_rank_detail_instance = DtoRankDetail.from_json(json)
# print the JSON string representation of the object
print(DtoRankDetail.to_json())

# convert the object into a dict
dto_rank_detail_dict = dto_rank_detail_instance.to_dict()
# create an instance of DtoRankDetail from a dict
dto_rank_detail_from_dict = DtoRankDetail.from_dict(dto_rank_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


