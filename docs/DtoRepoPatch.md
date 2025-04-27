# DtoRepoPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**topics** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.dto_repo_patch import DtoRepoPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepoPatch from a JSON string
dto_repo_patch_instance = DtoRepoPatch.from_json(json)
# print the JSON string representation of the object
print(DtoRepoPatch.to_json())

# convert the object into a dict
dto_repo_patch_dict = dto_repo_patch_instance.to_dict()
# create an instance of DtoRepoPatch from a dict
dto_repo_patch_from_dict = DtoRepoPatch.from_dict(dto_repo_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


