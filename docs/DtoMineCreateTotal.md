# DtoMineCreateTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_count** | **int** |  | [optional] 
**pull_request_count** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_mine_create_total import DtoMineCreateTotal

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMineCreateTotal from a JSON string
dto_mine_create_total_instance = DtoMineCreateTotal.from_json(json)
# print the JSON string representation of the object
print(DtoMineCreateTotal.to_json())

# convert the object into a dict
dto_mine_create_total_dict = dto_mine_create_total_instance.to_dict()
# create an instance of DtoMineCreateTotal from a dict
dto_mine_create_total_from_dict = DtoMineCreateTotal.from_dict(dto_mine_create_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


