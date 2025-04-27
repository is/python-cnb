# DtoStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | **int** | example: { \&quot;hard\&quot;: { \&quot;storage\&quot;: -1}},移除 omitempty ，Storage &#x3D; 0，会生成 {\&quot;hard\&quot;:{\&quot;storage\&quot;:0}} | [optional] 

## Example

```python
from cnb_api.models.dto_storage import DtoStorage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoStorage from a JSON string
dto_storage_instance = DtoStorage.from_json(json)
# print the JSON string representation of the object
print(DtoStorage.to_json())

# convert the object into a dict
dto_storage_dict = dto_storage_instance.to_dict()
# create an instance of DtoStorage from a dict
dto_storage_from_dict = DtoStorage.from_dict(dto_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


