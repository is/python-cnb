# WebCommitStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**target_url** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_status import WebCommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitStatus from a JSON string
web_commit_status_instance = WebCommitStatus.from_json(json)
# print the JSON string representation of the object
print(WebCommitStatus.to_json())

# convert the object into a dict
web_commit_status_dict = web_commit_status_instance.to_dict()
# create an instance of WebCommitStatus from a dict
web_commit_status_from_dict = WebCommitStatus.from_dict(web_commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


