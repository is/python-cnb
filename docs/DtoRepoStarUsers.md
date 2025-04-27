# DtoRepoStarUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_follow_count** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**users** | [**List[DtoStarUser]**](DtoStarUser.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_repo_star_users import DtoRepoStarUsers

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepoStarUsers from a JSON string
dto_repo_star_users_instance = DtoRepoStarUsers.from_json(json)
# print the JSON string representation of the object
print(DtoRepoStarUsers.to_json())

# convert the object into a dict
dto_repo_star_users_dict = dto_repo_star_users_instance.to_dict()
# create an instance of DtoRepoStarUsers from a dict
dto_repo_star_users_from_dict = DtoRepoStarUsers.from_dict(dto_repo_star_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


