# WebPullRequestRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_role** | **int** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**ref** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**usage** | [**WebRepositoryUsage**](WebRepositoryUsage.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_repository import WebPullRequestRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestRepository from a JSON string
web_pull_request_repository_instance = WebPullRequestRepository.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestRepository.to_json())

# convert the object into a dict
web_pull_request_repository_dict = web_pull_request_repository_instance.to_dict()
# create an instance of WebPullRequestRepository from a dict
web_pull_request_repository_from_dict = WebPullRequestRepository.from_dict(web_pull_request_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


