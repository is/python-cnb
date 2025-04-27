# DtoRepoRank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_type** | **str** |  | [optional] 
**repo_detail** | [**List[DtoRankDetail]**](DtoRankDetail.md) |  | [optional] 
**top_n** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_repo_rank import DtoRepoRank

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepoRank from a JSON string
dto_repo_rank_instance = DtoRepoRank.from_json(json)
# print the JSON string representation of the object
print(DtoRepoRank.to_json())

# convert the object into a dict
dto_repo_rank_dict = dto_repo_rank_instance.to_dict()
# create an instance of DtoRepoRank from a dict
dto_repo_rank_from_dict = DtoRepoRank.from_dict(dto_repo_rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


