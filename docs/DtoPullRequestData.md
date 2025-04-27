# DtoPullRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_issue_counts** | **int** |  | [optional] 
**build_status** | **str** |  | [optional] 
**comment_counts** | **int** |  | [optional] 
**created_time** | **str** |  | [optional] 
**label** | [**List[DtoLabel]**](DtoLabel.md) |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**slug** | **str** |  | [optional] 
**slug_freeze** | **bool** |  | [optional] 
**src_ref** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**target_ref** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**todo_id** | **str** |  | [optional] 
**updated_time** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_pull_request_data import DtoPullRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPullRequestData from a JSON string
dto_pull_request_data_instance = DtoPullRequestData.from_json(json)
# print the JSON string representation of the object
print(DtoPullRequestData.to_json())

# convert the object into a dict
dto_pull_request_data_dict = dto_pull_request_data_instance.to_dict()
# create an instance of DtoPullRequestData from a dict
dto_pull_request_data_from_dict = DtoPullRequestData.from_dict(dto_pull_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


