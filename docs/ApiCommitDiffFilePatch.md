# ApiCommitDiffFilePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** |  | [optional] 
**deletions** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**patch** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_commit_diff_file_patch import ApiCommitDiffFilePatch

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCommitDiffFilePatch from a JSON string
api_commit_diff_file_patch_instance = ApiCommitDiffFilePatch.from_json(json)
# print the JSON string representation of the object
print(ApiCommitDiffFilePatch.to_json())

# convert the object into a dict
api_commit_diff_file_patch_dict = api_commit_diff_file_patch_instance.to_dict()
# create an instance of ApiCommitDiffFilePatch from a dict
api_commit_diff_file_patch_from_dict = ApiCommitDiffFilePatch.from_dict(api_commit_diff_file_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


