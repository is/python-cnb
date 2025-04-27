# ApiMergePullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_message** | **str** |  | [optional] 
**commit_title** | **str** |  | [optional] 
**merge_style** | **str** | The merge method to use. Can be one of: &#x60;merge&#x60;, &#x60;squash&#x60;, &#x60;rebase&#x60; | [optional] 

## Example

```python
from cnb_api.models.api_merge_pull_request import ApiMergePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMergePullRequest from a JSON string
api_merge_pull_request_instance = ApiMergePullRequest.from_json(json)
# print the JSON string representation of the object
print(ApiMergePullRequest.to_json())

# convert the object into a dict
api_merge_pull_request_dict = api_merge_pull_request_instance.to_dict()
# create an instance of ApiMergePullRequest from a dict
api_merge_pull_request_from_dict = ApiMergePullRequest.from_dict(api_merge_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


