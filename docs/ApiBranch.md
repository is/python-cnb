# ApiBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**ApiBranchCommit**](ApiBranchCommit.md) |  | [optional] 
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.api_branch import ApiBranch

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBranch from a JSON string
api_branch_instance = ApiBranch.from_json(json)
# print the JSON string representation of the object
print(ApiBranch.to_json())

# convert the object into a dict
api_branch_dict = api_branch_instance.to_dict()
# create an instance of ApiBranch from a dict
api_branch_from_dict = ApiBranch.from_dict(api_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


