# DtoActivityDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_review_count** | **int** |  | [optional] 
**code_reviews** | [**List[DtoActivityRepoDetail]**](DtoActivityRepoDetail.md) |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commits** | [**List[DtoActivityRepoDetail]**](DtoActivityRepoDetail.md) |  | [optional] 
**group_count** | **int** |  | [optional] 
**groups** | [**List[DtoActivityJoinGroupDetail]**](DtoActivityJoinGroupDetail.md) |  | [optional] 
**issues** | [**List[DtoActivityRepoDetail]**](DtoActivityRepoDetail.md) |  | [optional] 
**issues_count** | **int** |  | [optional] 
**private_score** | **int** |  | [optional] 
**pull_request_count** | **int** |  | [optional] 
**pull_requests** | [**List[DtoActivityRepoDetail]**](DtoActivityRepoDetail.md) |  | [optional] 
**repo_count** | **int** |  | [optional] 
**repos** | [**List[DtoActivityCreateRepoDetail]**](DtoActivityCreateRepoDetail.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_date import DtoActivityDate

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityDate from a JSON string
dto_activity_date_instance = DtoActivityDate.from_json(json)
# print the JSON string representation of the object
print(DtoActivityDate.to_json())

# convert the object into a dict
dto_activity_date_dict = dto_activity_date_instance.to_dict()
# create an instance of DtoActivityDate from a dict
dto_activity_date_from_dict = DtoActivityDate.from_dict(dto_activity_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


