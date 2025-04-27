# WebTreeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[WebTreeInfoEntry]**](WebTreeInfoEntry.md) |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_tree_info import WebTreeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebTreeInfo from a JSON string
web_tree_info_instance = WebTreeInfo.from_json(json)
# print the JSON string representation of the object
print(WebTreeInfo.to_json())

# convert the object into a dict
web_tree_info_dict = web_tree_info_instance.to_dict()
# create an instance of WebTreeInfo from a dict
web_tree_info_from_dict = WebTreeInfo.from_dict(web_tree_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


