# ApiPullRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | [optional] 
**repo** | [**ApiRepo**](ApiRepo.md) |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_ref import ApiPullRef

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullRef from a JSON string
api_pull_ref_instance = ApiPullRef.from_json(json)
# print the JSON string representation of the object
print(ApiPullRef.to_json())

# convert the object into a dict
api_pull_ref_dict = api_pull_ref_instance.to_dict()
# create an instance of ApiPullRef from a dict
api_pull_ref_from_dict = ApiPullRef.from_dict(api_pull_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


