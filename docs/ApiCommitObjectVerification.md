# ApiCommitObjectVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 
**resone** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.api_commit_object_verification import ApiCommitObjectVerification

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCommitObjectVerification from a JSON string
api_commit_object_verification_instance = ApiCommitObjectVerification.from_json(json)
# print the JSON string representation of the object
print(ApiCommitObjectVerification.to_json())

# convert the object into a dict
api_commit_object_verification_dict = api_commit_object_verification_instance.to_dict()
# create an instance of ApiCommitObjectVerification from a dict
api_commit_object_verification_from_dict = ApiCommitObjectVerification.from_dict(api_commit_object_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


