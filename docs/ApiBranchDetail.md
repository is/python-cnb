# ApiBranchDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**ApiCommit**](ApiCommit.md) |  | [optional] 
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.api_branch_detail import ApiBranchDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBranchDetail from a JSON string
api_branch_detail_instance = ApiBranchDetail.from_json(json)
# print the JSON string representation of the object
print(ApiBranchDetail.to_json())

# convert the object into a dict
api_branch_detail_dict = api_branch_detail_instance.to_dict()
# create an instance of ApiBranchDetail from a dict
api_branch_detail_from_dict = ApiBranchDetail.from_dict(api_branch_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


