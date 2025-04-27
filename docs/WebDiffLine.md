# WebDiffLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**left_line_number** | **int** |  | [optional] 
**prefix** | **str** |  | [optional] 
**right_line_number** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_diff_line import WebDiffLine

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiffLine from a JSON string
web_diff_line_instance = WebDiffLine.from_json(json)
# print the JSON string representation of the object
print(WebDiffLine.to_json())

# convert the object into a dict
web_diff_line_dict = web_diff_line_instance.to_dict()
# create an instance of WebDiffLine from a dict
web_diff_line_from_dict = WebDiffLine.from_dict(web_diff_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


