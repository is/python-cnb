# WebDiff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**file_exceeded** | **bool** |  | [optional] 
**file_limit** | **int** |  | [optional] 
**files** | [**List[WebDiffFile]**](WebDiffFile.md) |  | [optional] 
**head_commit** | **str** |  | [optional] 
**stat** | [**WebDiffStat**](WebDiffStat.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_diff import WebDiff

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiff from a JSON string
web_diff_instance = WebDiff.from_json(json)
# print the JSON string representation of the object
print(WebDiff.to_json())

# convert the object into a dict
web_diff_dict = web_diff_instance.to_dict()
# create an instance of WebDiff from a dict
web_diff_from_dict = WebDiff.from_dict(web_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


