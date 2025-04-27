# WebBranchPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_merged** | **bool** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_branch_pull_request import WebBranchPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebBranchPullRequest from a JSON string
web_branch_pull_request_instance = WebBranchPullRequest.from_json(json)
# print the JSON string representation of the object
print(WebBranchPullRequest.to_json())

# convert the object into a dict
web_branch_pull_request_dict = web_branch_pull_request_instance.to_dict()
# create an instance of WebBranchPullRequest from a dict
web_branch_pull_request_from_dict = WebBranchPullRequest.from_dict(web_branch_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


