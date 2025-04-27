# ScopeScene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.scope_scene import ScopeScene

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeScene from a JSON string
scope_scene_instance = ScopeScene.from_json(json)
# print the JSON string representation of the object
print(ScopeScene.to_json())

# convert the object into a dict
scope_scene_dict = scope_scene_instance.to_dict()
# create an instance of ScopeScene from a dict
scope_scene_from_dict = ScopeScene.from_dict(scope_scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


