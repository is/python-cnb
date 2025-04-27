# DtoSpecialAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_build_corehour** | **int** |  | [optional] 
**compute_build_desc** | **str** |  | [optional] 
**compute_build_expire** | **str** |  | [optional] 
**compute_develop_corehour** | **int** |  | [optional] 
**compute_develop_desc** | **str** |  | [optional] 
**compute_develop_expire** | **str** |  | [optional] 
**storage_git_desc** | **str** |  | [optional] 
**storage_git_expire** | **str** |  | [optional] 
**storage_git_gib** | **int** |  | [optional] 
**storage_object_desc** | **str** |  | [optional] 
**storage_object_expire** | **str** |  | [optional] 
**storage_object_gib** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_special_amount import DtoSpecialAmount

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSpecialAmount from a JSON string
dto_special_amount_instance = DtoSpecialAmount.from_json(json)
# print the JSON string representation of the object
print(DtoSpecialAmount.to_json())

# convert the object into a dict
dto_special_amount_dict = dto_special_amount_instance.to_dict()
# create an instance of DtoSpecialAmount from a dict
dto_special_amount_from_dict = DtoSpecialAmount.from_dict(dto_special_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


