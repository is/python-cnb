# WebComparedCommits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | **str** |  | [optional] 
**commit_count** | **int** |  | [optional] 
**commits** | [**List[WebCommit]**](WebCommit.md) |  | [optional] 
**head_commit** | **str** |  | [optional] 
**merge_base_commit** | **str** |  | [optional] 
**straight** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_compared_commits import WebComparedCommits

# TODO update the JSON string below
json = "{}"
# create an instance of WebComparedCommits from a JSON string
web_compared_commits_instance = WebComparedCommits.from_json(json)
# print the JSON string representation of the object
print(WebComparedCommits.to_json())

# convert the object into a dict
web_compared_commits_dict = web_compared_commits_instance.to_dict()
# create an instance of WebComparedCommits from a dict
web_compared_commits_from_dict = WebComparedCommits.from_dict(web_compared_commits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


