# WebRepositoryUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_size_in_kib** | **str** |  | [optional] 
**lfs_size_in_kib** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_repository_usage import WebRepositoryUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WebRepositoryUsage from a JSON string
web_repository_usage_instance = WebRepositoryUsage.from_json(json)
# print the JSON string representation of the object
print(WebRepositoryUsage.to_json())

# convert the object into a dict
web_repository_usage_dict = web_repository_usage_instance.to_dict()
# create an instance of WebRepositoryUsage from a dict
web_repository_usage_from_dict = WebRepositoryUsage.from_dict(web_repository_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


