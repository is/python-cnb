# WebComparedRawDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**diff** | **str** |  | [optional] 
**head_commit** | **str** |  | [optional] 
**merge_base_commit** | **str** |  | [optional] 
**straight** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_compared_raw_diff import WebComparedRawDiff

# TODO update the JSON string below
json = "{}"
# create an instance of WebComparedRawDiff from a JSON string
web_compared_raw_diff_instance = WebComparedRawDiff.from_json(json)
# print the JSON string representation of the object
print(WebComparedRawDiff.to_json())

# convert the object into a dict
web_compared_raw_diff_dict = web_compared_raw_diff_instance.to_dict()
# create an instance of WebComparedRawDiff from a dict
web_compared_raw_diff_from_dict = WebComparedRawDiff.from_dict(web_compared_raw_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


