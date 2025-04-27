# ApiPatchPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**state** | **str** | State of this Pull Request. Either &#x60;open&#x60; or &#x60;closed&#x60;. | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_patch_pull_request import ApiPatchPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPatchPullRequest from a JSON string
api_patch_pull_request_instance = ApiPatchPullRequest.from_json(json)
# print the JSON string representation of the object
print(ApiPatchPullRequest.to_json())

# convert the object into a dict
api_patch_pull_request_dict = api_patch_pull_request_instance.to_dict()
# create an instance of ApiPatchPullRequest from a dict
api_patch_pull_request_from_dict = ApiPatchPullRequest.from_dict(api_patch_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


