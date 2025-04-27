# WebRefWithPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initialized** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**ref_simple_name** | **str** |  | [optional] 
**ref_type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_ref_with_path import WebRefWithPath

# TODO update the JSON string below
json = "{}"
# create an instance of WebRefWithPath from a JSON string
web_ref_with_path_instance = WebRefWithPath.from_json(json)
# print the JSON string representation of the object
print(WebRefWithPath.to_json())

# convert the object into a dict
web_ref_with_path_dict = web_ref_with_path_instance.to_dict()
# create an instance of WebRefWithPath from a dict
web_ref_with_path_from_dict = WebRefWithPath.from_dict(web_ref_with_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


