# ApiRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_repo import ApiRepo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRepo from a JSON string
api_repo_instance = ApiRepo.from_json(json)
# print the JSON string representation of the object
print(ApiRepo.to_json())

# convert the object into a dict
api_repo_dict = api_repo_instance.to_dict()
# create an instance of ApiRepo from a dict
api_repo_from_dict = ApiRepo.from_dict(api_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


