# DtoMavenPackageDetail


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
**tags** | [**List[DtoMavenTag]**](DtoMavenTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_maven_package_detail import DtoMavenPackageDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMavenPackageDetail from a JSON string
dto_maven_package_detail_instance = DtoMavenPackageDetail.from_json(json)
# print the JSON string representation of the object
print(DtoMavenPackageDetail.to_json())

# convert the object into a dict
dto_maven_package_detail_dict = dto_maven_package_detail_instance.to_dict()
# create an instance of DtoMavenPackageDetail from a dict
dto_maven_package_detail_from_dict = DtoMavenPackageDetail.from_dict(dto_maven_package_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


