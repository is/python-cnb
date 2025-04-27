# WebForkSyncStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ahead** | **int** |  | [optional] 
**behind** | **int** |  | [optional] 
**upstream_ref** | **str** |  | [optional] 
**upstream_slug** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_fork_sync_status import WebForkSyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebForkSyncStatus from a JSON string
web_fork_sync_status_instance = WebForkSyncStatus.from_json(json)
# print the JSON string representation of the object
print(WebForkSyncStatus.to_json())

# convert the object into a dict
web_fork_sync_status_dict = web_fork_sync_status_instance.to_dict()
# create an instance of WebForkSyncStatus from a dict
web_fork_sync_status_from_dict = WebForkSyncStatus.from_dict(web_fork_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


