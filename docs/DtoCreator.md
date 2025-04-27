# DtoCreator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freeze** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_creator import DtoCreator

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreator from a JSON string
dto_creator_instance = DtoCreator.from_json(json)
# print the JSON string representation of the object
print(DtoCreator.to_json())

# convert the object into a dict
dto_creator_dict = dto_creator_instance.to_dict()
# create an instance of DtoCreator from a dict
dto_creator_from_dict = DtoCreator.from_dict(dto_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


