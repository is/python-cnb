# ApiCommitObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**ApiSignature**](ApiSignature.md) |  | [optional] 
**comment_count** | **int** |  | [optional] 
**committer** | [**ApiSignature**](ApiSignature.md) |  | [optional] 
**message** | **str** |  | [optional] 
**tree** | [**ApiCommitObjectTree**](ApiCommitObjectTree.md) |  | [optional] 
**verification** | [**ApiCommitObjectVerification**](ApiCommitObjectVerification.md) |  | [optional] 

## Example

```python
from cnb_api.models.api_commit_object import ApiCommitObject

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCommitObject from a JSON string
api_commit_object_instance = ApiCommitObject.from_json(json)
# print the JSON string representation of the object
print(ApiCommitObject.to_json())

# convert the object into a dict
api_commit_object_dict = api_commit_object_instance.to_dict()
# create an instance of ApiCommitObject from a dict
api_commit_object_from_dict = ApiCommitObject.from_dict(api_commit_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


