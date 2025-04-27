# WebCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo.md) |  | [optional] 
**commit** | [**WebCommitObject**](WebCommitObject.md) |  | [optional] 
**commit_statuses** | [**WebCommitStatuses**](WebCommitStatuses.md) |  | [optional] 
**committer** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo.md) |  | [optional] 
**files** | [**WebCommitFiles**](WebCommitFiles.md) |  | [optional] 
**parents** | [**List[WebCommitParent]**](WebCommitParent.md) |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit import WebCommit

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommit from a JSON string
web_commit_instance = WebCommit.from_json(json)
# print the JSON string representation of the object
print(WebCommit.to_json())

# convert the object into a dict
web_commit_dict = web_commit_instance.to_dict()
# create an instance of WebCommit from a dict
web_commit_from_dict = WebCommit.from_dict(web_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


