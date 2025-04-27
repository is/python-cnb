# DtoFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_file import DtoFile

# TODO update the JSON string below
json = "{}"
# create an instance of DtoFile from a JSON string
dto_file_instance = DtoFile.from_json(json)
# print the JSON string representation of the object
print(DtoFile.to_json())

# convert the object into a dict
dto_file_dict = dto_file_instance.to_dict()
# create an instance of DtoFile from a dict
dto_file_from_dict = DtoFile.from_dict(dto_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


