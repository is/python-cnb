# ApiIssueComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo**](GitWoaComCnbMonorepoGitInternalAppVcsServiceBffApiUserInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_issue_comment import ApiIssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of ApiIssueComment from a JSON string
api_issue_comment_instance = ApiIssueComment.from_json(json)
# print the JSON string representation of the object
print(ApiIssueComment.to_json())

# convert the object into a dict
api_issue_comment_dict = api_issue_comment_instance.to_dict()
# create an instance of ApiIssueComment from a dict
api_issue_comment_from_dict = ApiIssueComment.from_dict(api_issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


