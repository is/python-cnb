# WebPullRequestFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**diff** | [**WebDiff**](WebDiff.md) |  | [optional] 
**file_comments** | [**List[WebPullRequestFileComments]**](WebPullRequestFileComments.md) |  | [optional] 
**head_commit** | **str** |  | [optional] 
**merge_base_commit** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_files import WebPullRequestFiles

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestFiles from a JSON string
web_pull_request_files_instance = WebPullRequestFiles.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestFiles.to_json())

# convert the object into a dict
web_pull_request_files_dict = web_pull_request_files_instance.to_dict()
# create an instance of WebPullRequestFiles from a dict
web_pull_request_files_from_dict = WebPullRequestFiles.from_dict(web_pull_request_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


