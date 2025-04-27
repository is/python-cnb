# DtoCreateRegistryReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_policy** | **str** |  | [optional] [default to 'all']
**description** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**overwrite_policy** | **str** |  | [optional] [default to 'forbid']
**visibility** | **str** |  | [optional] [default to 'public']

## Example

```python
from cnb_api.models.dto_create_registry_req import DtoCreateRegistryReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateRegistryReq from a JSON string
dto_create_registry_req_instance = DtoCreateRegistryReq.from_json(json)
# print the JSON string representation of the object
print(DtoCreateRegistryReq.to_json())

# convert the object into a dict
dto_create_registry_req_dict = dto_create_registry_req_instance.to_dict()
# create an instance of DtoCreateRegistryReq from a dict
dto_create_registry_req_from_dict = DtoCreateRegistryReq.from_dict(dto_create_registry_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


