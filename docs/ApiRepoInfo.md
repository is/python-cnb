# ApiRepoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_repo_info import ApiRepoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRepoInfo from a JSON string
api_repo_info_instance = ApiRepoInfo.from_json(json)
# print the JSON string representation of the object
print(ApiRepoInfo.to_json())

# convert the object into a dict
api_repo_info_dict = api_repo_info_instance.to_dict()
# create an instance of ApiRepoInfo from a dict
api_repo_info_from_dict = ApiRepoInfo.from_dict(api_repo_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


