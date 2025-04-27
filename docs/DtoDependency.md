# DtoDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_dependency import DtoDependency

# TODO update the JSON string below
json = "{}"
# create an instance of DtoDependency from a JSON string
dto_dependency_instance = DtoDependency.from_json(json)
# print the JSON string representation of the object
print(DtoDependency.to_json())

# convert the object into a dict
dto_dependency_dict = dto_dependency_instance.to_dict()
# create an instance of DtoDependency from a dict
dto_dependency_from_dict = DtoDependency.from_dict(dto_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


