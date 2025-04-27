# DtoIssueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_pull_request_counts** | **int** |  | [optional] 
**comment_counts** | **int** |  | [optional] 
**created_time** | **str** |  | [optional] 
**creator** | [**DtoCreator**](DtoCreator.md) |  | [optional] 
**label** | [**List[DtoLabel]**](DtoLabel.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**priority** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**slug_freeze** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**todo_id** | **str** |  | [optional] 
**updated_time** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_issue_data import DtoIssueData

# TODO update the JSON string below
json = "{}"
# create an instance of DtoIssueData from a JSON string
dto_issue_data_instance = DtoIssueData.from_json(json)
# print the JSON string representation of the object
print(DtoIssueData.to_json())

# convert the object into a dict
dto_issue_data_dict = dto_issue_data_instance.to_dict()
# create an instance of DtoIssueData from a dict
dto_issue_data_from_dict = DtoIssueData.from_dict(dto_issue_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


