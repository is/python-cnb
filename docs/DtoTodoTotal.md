# DtoTodoTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_complete_count** | **int** |  | [optional] 
**issue_pending_count** | **int** |  | [optional] 
**pull_request_complete_count** | **int** |  | [optional] 
**pull_request_pending_count** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_todo_total import DtoTodoTotal

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTodoTotal from a JSON string
dto_todo_total_instance = DtoTodoTotal.from_json(json)
# print the JSON string representation of the object
print(DtoTodoTotal.to_json())

# convert the object into a dict
dto_todo_total_dict = dto_todo_total_instance.to_dict()
# create an instance of DtoTodoTotal from a dict
dto_todo_total_from_dict = DtoTodoTotal.from_dict(dto_todo_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


