# ApiMergePullResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_merge_pull_response import ApiMergePullResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMergePullResponse from a JSON string
api_merge_pull_response_instance = ApiMergePullResponse.from_json(json)
# print the JSON string representation of the object
print(ApiMergePullResponse.to_json())

# convert the object into a dict
api_merge_pull_response_dict = api_merge_pull_response_instance.to_dict()
# create an instance of ApiMergePullResponse from a dict
api_merge_pull_response_from_dict = ApiMergePullResponse.from_dict(api_merge_pull_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


