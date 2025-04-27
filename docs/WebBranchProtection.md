# WebBranchProtection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_creation** | **bool** |  | [optional] 
**allow_deletions** | **bool** |  | [optional] 
**allow_force_pushes** | **bool** |  | [optional] 
**allow_master_creation** | **bool** |  | [optional] 
**allow_master_deletions** | **bool** |  | [optional] 
**allow_master_force_pushes** | **bool** |  | [optional] 
**allow_master_pushes** | **bool** |  | [optional] 
**allow_pushes** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**match_count** | **int** |  | [optional] 
**required_approved_review_count** | **int** |  | [optional] 
**required_approved_review_ratio** | **int** |  | [optional] 
**required_commit_signatures** | **bool** |  | [optional] 
**required_linear_history** | **bool** |  | [optional] 
**required_master_approve** | **bool** |  | [optional] 
**required_must_auto_merge** | **bool** |  | [optional] 
**required_must_push_via_pull_request** | **bool** |  | [optional] 
**required_pull_request_reviews** | **bool** |  | [optional] 
**required_status_checks** | **bool** |  | [optional] 
**rule** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_branch_protection import WebBranchProtection

# TODO update the JSON string below
json = "{}"
# create an instance of WebBranchProtection from a JSON string
web_branch_protection_instance = WebBranchProtection.from_json(json)
# print the JSON string representation of the object
print(WebBranchProtection.to_json())

# convert the object into a dict
web_branch_protection_dict = web_branch_protection_instance.to_dict()
# create an instance of WebBranchProtection from a dict
web_branch_protection_from_dict = WebBranchProtection.from_dict(web_branch_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


