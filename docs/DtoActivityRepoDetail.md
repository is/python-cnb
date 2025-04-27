# DtoActivityRepoDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**DtoActivitySlugDetail**](DtoActivitySlugDetail.md) | 公仓转私仓或仓库被删除后为 null | [optional] 
**exposed_repo_path** | **str** | activity 发生时仓库的 path，这时的 path 是可以公开的 | [optional] 
**freeze** | **bool** | 仓库是否封禁 | [optional] 
**repo_unaccessible** | **bool** | 仓库是否不可访问（公仓转私仓或仓库被删除后不可访问） | [optional] 
**time** | **float** |  | [optional] 
**visibility_level** | [**ConstantVisibility**](ConstantVisibility.md) | 仓库可见性 | [optional] 

## Example

```python
from cnb_api.models.dto_activity_repo_detail import DtoActivityRepoDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityRepoDetail from a JSON string
dto_activity_repo_detail_instance = DtoActivityRepoDetail.from_json(json)
# print the JSON string representation of the object
print(DtoActivityRepoDetail.to_json())

# convert the object into a dict
dto_activity_repo_detail_dict = dto_activity_repo_detail_instance.to_dict()
# create an instance of DtoActivityRepoDetail from a dict
dto_activity_repo_detail_from_dict = DtoActivityRepoDetail.from_dict(dto_activity_repo_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


