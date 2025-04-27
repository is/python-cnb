# WebRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_ref** | **str** |  | [optional] 
**http_clone_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**ssh_clone_url** | **str** |  | [optional] 
**usage** | [**WebRepositoryUsage**](WebRepositoryUsage.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_repository import WebRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebRepository from a JSON string
web_repository_instance = WebRepository.from_json(json)
# print the JSON string representation of the object
print(WebRepository.to_json())

# convert the object into a dict
web_repository_dict = web_repository_instance.to_dict()
# create an instance of WebRepository from a dict
web_repository_from_dict = WebRepository.from_dict(web_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


