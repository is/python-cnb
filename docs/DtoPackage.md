# DtoPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**last_artifact_name** | **str** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**name** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**package_type** | [**DtoPackageType**](DtoPackageType.md) |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_package import DtoPackage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPackage from a JSON string
dto_package_instance = DtoPackage.from_json(json)
# print the JSON string representation of the object
print(DtoPackage.to_json())

# convert the object into a dict
dto_package_dict = dto_package_instance.to_dict()
# create an instance of DtoPackage from a dict
dto_package_from_dict = DtoPackage.from_dict(dto_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


