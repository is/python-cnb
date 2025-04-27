# WebLastPushBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **str** |  | [optional] 
**is_head** | **bool** |  | [optional] 
**pull_number** | **int** |  | [optional] 
**ref** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_last_push_branch import WebLastPushBranch

# TODO update the JSON string below
json = "{}"
# create an instance of WebLastPushBranch from a JSON string
web_last_push_branch_instance = WebLastPushBranch.from_json(json)
# print the JSON string representation of the object
print(WebLastPushBranch.to_json())

# convert the object into a dict
web_last_push_branch_dict = web_last_push_branch_instance.to_dict()
# create an instance of WebLastPushBranch from a dict
web_last_push_branch_from_dict = WebLastPushBranch.from_dict(web_last_push_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


