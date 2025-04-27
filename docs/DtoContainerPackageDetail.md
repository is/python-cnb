# DtoContainerPackageDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**package** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**tag_total** | **int** |  | [optional] 
**tags** | [**List[DtoContainerTag]**](DtoContainerTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_package_detail import DtoContainerPackageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerPackageDetail from a JSON string
dto_container_package_detail_instance = DtoContainerPackageDetail.from_json(json)
# print the JSON string representation of the object
print(DtoContainerPackageDetail.to_json())

# convert the object into a dict
dto_container_package_detail_dict = dto_container_package_detail_instance.to_dict()
# create an instance of DtoContainerPackageDetail from a dict
dto_container_package_detail_from_dict = DtoContainerPackageDetail.from_dict(dto_container_package_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


