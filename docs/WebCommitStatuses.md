# WebCommitStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**statuses** | [**List[WebCommitStatus]**](WebCommitStatus.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_statuses import WebCommitStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitStatuses from a JSON string
web_commit_statuses_instance = WebCommitStatuses.from_json(json)
# print the JSON string representation of the object
print(WebCommitStatuses.to_json())

# convert the object into a dict
web_commit_statuses_dict = web_commit_statuses_instance.to_dict()
# create an instance of WebCommitStatuses from a dict
web_commit_statuses_from_dict = WebCommitStatuses.from_dict(web_commit_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


