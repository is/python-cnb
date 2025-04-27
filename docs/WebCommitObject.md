# WebCommitObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebSignature**](WebSignature.md) |  | [optional] 
**comment_count** | **int** |  | [optional] 
**committer** | [**WebSignature**](WebSignature.md) |  | [optional] 
**message** | **str** |  | [optional] 
**tree** | [**WebCommitObjectTree**](WebCommitObjectTree.md) |  | [optional] 
**verification** | [**WebCommitObjectVerification**](WebCommitObjectVerification.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_object import WebCommitObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitObject from a JSON string
web_commit_object_instance = WebCommitObject.from_json(json)
# print the JSON string representation of the object
print(WebCommitObject.to_json())

# convert the object into a dict
web_commit_object_dict = web_commit_object_instance.to_dict()
# create an instance of WebCommitObject from a dict
web_commit_object_from_dict = WebCommitObject.from_dict(web_commit_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


