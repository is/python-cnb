# WebFileContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_count** | **int** |  | [optional] 
**cnb_settings** | [**WebPreloadFile**](WebPreloadFile.md) |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commit_count_exceeded** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**file_size_exceeded** | **bool** |  | [optional] 
**file_size_limit** | **int** |  | [optional] 
**file_stat** | [**WebFileStat**](WebFileStat.md) |  | [optional] 
**initialized** | **bool** |  | [optional] 
**is_lfs** | **bool** |  | [optional] 
**is_protected** | **bool** | 如果当前访问的是分支，那么表示是否是保护分支 | [optional] 
**last_commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**lfs_hash_algorithm** | **str** |  | [optional] 
**lfs_oid** | **str** |  | [optional] 
**lfs_size_in_byte** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**repository** | [**WebRepository**](WebRepository.md) |  | [optional] 
**size** | **int** |  | [optional] 
**tag_count** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_file_content import WebFileContent

# TODO update the JSON string below
json = "{}"
# create an instance of WebFileContent from a JSON string
web_file_content_instance = WebFileContent.from_json(json)
# print the JSON string representation of the object
print(WebFileContent.to_json())

# convert the object into a dict
web_file_content_dict = web_file_content_instance.to_dict()
# create an instance of WebFileContent from a dict
web_file_content_from_dict = WebFileContent.from_dict(web_file_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


