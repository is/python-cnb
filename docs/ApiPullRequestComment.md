# ApiPullRequestComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_request_comment import ApiPullRequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRequestComment from a JSON string
api_pull_request_comment_instance = ApiPullRequestComment.from_json(json)
# print the JSON string representation of the object
print(ApiPullRequestComment.to_json())

# convert the object into a dict
api_pull_request_comment_dict = api_pull_request_comment_instance.to_dict()
# create an instance of ApiPullRequestComment from a dict
api_pull_request_comment_from_dict = ApiPullRequestComment.from_dict(api_pull_request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


