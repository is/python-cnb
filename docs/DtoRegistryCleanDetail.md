# DtoRegistryCleanDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_num** | **int** |  | [optional] 
**clean_policy** | [**DtoCleanPolicy**](DtoCleanPolicy.md) |  | [optional] 
**status** | [**DtoCleanPolicyStatus**](DtoCleanPolicyStatus.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_registry_clean_detail import DtoRegistryCleanDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRegistryCleanDetail from a JSON string
dto_registry_clean_detail_instance = DtoRegistryCleanDetail.from_json(json)
# print the JSON string representation of the object
print(DtoRegistryCleanDetail.to_json())

# convert the object into a dict
dto_registry_clean_detail_dict = dto_registry_clean_detail_instance.to_dict()
# create an instance of DtoRegistryCleanDetail from a dict
dto_registry_clean_detail_from_dict = DtoRegistryCleanDetail.from_dict(dto_registry_clean_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


