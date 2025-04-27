# WebTreeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_count** | **int** |  | [optional] 
**cnb_settings** | [**WebPreloadFile**](WebPreloadFile.md) |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commit_count_exceeded** | **bool** |  | [optional] 
**entries** | [**List[WebTreeEntry]**](WebTreeEntry.md) |  | [optional] 
**file_list_exceeded** | **bool** |  | [optional] 
**file_list_limit** | **int** |  | [optional] 
**has_web_trigger** | **bool** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**is_protected** | **bool** | 如果当前访问的是分支，那么表示是否是保护分支 | [optional] 
**last_commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**read_me** | [**WebPreloadFile**](WebPreloadFile.md) |  | [optional] 
**repository** | [**WebRepository**](WebRepository.md) |  | [optional] 
**tag_count** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_tree_content import WebTreeContent

# TODO update the JSON string below
json = "{}"
# create an instance of WebTreeContent from a JSON string
web_tree_content_instance = WebTreeContent.from_json(json)
# print the JSON string representation of the object
print(WebTreeContent.to_json())

# convert the object into a dict
web_tree_content_dict = web_tree_content_instance.to_dict()
# create an instance of WebTreeContent from a dict
web_tree_content_from_dict = WebTreeContent.from_dict(web_tree_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


