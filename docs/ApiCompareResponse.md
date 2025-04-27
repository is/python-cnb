# ApiCompareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_commit** | [**ApiCommit**](ApiCommit.md) |  | [optional] 
**commits** | [**List[ApiCommit]**](ApiCommit.md) |  | [optional] 
**files** | [**List[ApiCommitDiffFilePatch]**](ApiCommitDiffFilePatch.md) |  | [optional] 
**head_commit** | [**ApiCommit**](ApiCommit.md) |  | [optional] 
**merge_base_commit** | [**ApiCommit**](ApiCommit.md) |  | [optional] 
**total_commits** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.api_compare_response import ApiCompareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCompareResponse from a JSON string
api_compare_response_instance = ApiCompareResponse.from_json(json)
# print the JSON string representation of the object
print(ApiCompareResponse.to_json())

# convert the object into a dict
api_compare_response_dict = api_compare_response_instance.to_dict()
# create an instance of ApiCompareResponse from a dict
api_compare_response_from_dict = ApiCompareResponse.from_dict(api_compare_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


