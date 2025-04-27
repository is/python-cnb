# ApiPullRefInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | [optional] 
**repo** | [**ApiRepoInfo**](ApiRepoInfo.md) |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_ref_info import ApiPullRefInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRefInfo from a JSON string
api_pull_ref_info_instance = ApiPullRefInfo.from_json(json)
# print the JSON string representation of the object
print(ApiPullRefInfo.to_json())

# convert the object into a dict
api_pull_ref_info_dict = api_pull_ref_info_instance.to_dict()
# create an instance of ApiPullRefInfo from a dict
api_pull_ref_info_from_dict = ApiPullRefInfo.from_dict(api_pull_ref_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


