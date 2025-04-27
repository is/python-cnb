# WebMissionResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | [**List[WebIssueResource]**](WebIssueResource.md) |  | [optional] 
**pull_requests** | [**List[WebPullRequestResource]**](WebPullRequestResource.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_mission_resources import WebMissionResources

# TODO update the JSON string below
json = "{}"
# create an instance of WebMissionResources from a JSON string
web_mission_resources_instance = WebMissionResources.from_json(json)
# print the JSON string representation of the object
print(WebMissionResources.to_json())

# convert the object into a dict
web_mission_resources_dict = web_mission_resources_instance.to_dict()
# create an instance of WebMissionResources from a dict
web_mission_resources_from_dict = WebMissionResources.from_dict(web_mission_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


