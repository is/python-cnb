# WebPullViewedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_commit_sha** | **str** |  | [optional] 
**is_viewed** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_viewed_file import WebPullViewedFile

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullViewedFile from a JSON string
web_pull_viewed_file_instance = WebPullViewedFile.from_json(json)
# print the JSON string representation of the object
print(WebPullViewedFile.to_json())

# convert the object into a dict
web_pull_viewed_file_dict = web_pull_viewed_file_instance.to_dict()
# create an instance of WebPullViewedFile from a dict
web_pull_viewed_file_from_dict = WebPullViewedFile.from_dict(web_pull_viewed_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


