# DtoActivityRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hash** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_release import DtoActivityRelease

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityRelease from a JSON string
dto_activity_release_instance = DtoActivityRelease.from_json(json)
# print the JSON string representation of the object
print(DtoActivityRelease.to_json())

# convert the object into a dict
dto_activity_release_dict = dto_activity_release_instance.to_dict()
# create an instance of DtoActivityRelease from a dict
dto_activity_release_from_dict = DtoActivityRelease.from_dict(dto_activity_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


