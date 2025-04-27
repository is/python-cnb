# DtoResourceBindInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**expire_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_resource_bind_info import DtoResourceBindInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoResourceBindInfo from a JSON string
dto_resource_bind_info_instance = DtoResourceBindInfo.from_json(json)
# print the JSON string representation of the object
print(DtoResourceBindInfo.to_json())

# convert the object into a dict
dto_resource_bind_info_dict = dto_resource_bind_info_instance.to_dict()
# create an instance of DtoResourceBindInfo from a dict
dto_resource_bind_info_from_dict = DtoResourceBindInfo.from_dict(dto_resource_bind_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


