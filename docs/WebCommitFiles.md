# WebCommitFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**diff** | [**WebDiff**](WebDiff.md) |  | [optional] 
**head_commit** | **str** |  | [optional] 
**straight** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_files import WebCommitFiles

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitFiles from a JSON string
web_commit_files_instance = WebCommitFiles.from_json(json)
# print the JSON string representation of the object
print(WebCommitFiles.to_json())

# convert the object into a dict
web_commit_files_dict = web_commit_files_instance.to_dict()
# create an instance of WebCommitFiles from a dict
web_commit_files_from_dict = WebCommitFiles.from_dict(web_commit_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


