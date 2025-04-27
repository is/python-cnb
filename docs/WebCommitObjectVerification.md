# WebCommitObjectVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_object_verification import WebCommitObjectVerification

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitObjectVerification from a JSON string
web_commit_object_verification_instance = WebCommitObjectVerification.from_json(json)
# print the JSON string representation of the object
print(WebCommitObjectVerification.to_json())

# convert the object into a dict
web_commit_object_verification_dict = web_commit_object_verification_instance.to_dict()
# create an instance of WebCommitObjectVerification from a dict
web_commit_object_verification_from_dict = WebCommitObjectVerification.from_dict(web_commit_object_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


