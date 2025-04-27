# ApiCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**commit** | [**ApiCommitObject**](ApiCommitObject.md) |  | [optional] 
**committer** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffApiUserInfo.md) |  | [optional] 
**parents** | [**List[ApiCommitParent]**](ApiCommitParent.md) |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_commit import ApiCommit

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCommit from a JSON string
api_commit_instance = ApiCommit.from_json(json)
# print the JSON string representation of the object
print(ApiCommit.to_json())

# convert the object into a dict
api_commit_dict = api_commit_instance.to_dict()
# create an instance of ApiCommit from a dict
api_commit_from_dict = ApiCommit.from_dict(api_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


