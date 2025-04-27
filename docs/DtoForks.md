# DtoForks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**fork_count** | **int** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**nickname** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**user_freeze** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_forks import DtoForks

# TODO update the JSON string below
json = "{}"
# create an instance of DtoForks from a JSON string
dto_forks_instance = DtoForks.from_json(json)
# print the JSON string representation of the object
print(DtoForks.to_json())

# convert the object into a dict
dto_forks_dict = dto_forks_instance.to_dict()
# create an instance of DtoForks from a dict
dto_forks_from_dict = DtoForks.from_dict(dto_forks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


