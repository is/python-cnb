# ApiCommitStatus


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
from cnb_api.models.api_commit_status import ApiCommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCommitStatus from a JSON string
api_commit_status_instance = ApiCommitStatus.from_json(json)
# print the JSON string representation of the object
print(ApiCommitStatus.to_json())

# convert the object into a dict
api_commit_status_dict = api_commit_status_instance.to_dict()
# create an instance of ApiCommitStatus from a dict
api_commit_status_from_dict = ApiCommitStatus.from_dict(api_commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


