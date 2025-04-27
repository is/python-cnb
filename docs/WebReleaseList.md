# WebReleaseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_count** | **int** |  | [optional] 
**releases** | [**List[WebRelease]**](WebRelease.md) |  | [optional] 
**tag_count** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_release_list import WebReleaseList

# TODO update the JSON string below
json = "{}"
# create an instance of WebReleaseList from a JSON string
web_release_list_instance = WebReleaseList.from_json(json)
# print the JSON string representation of the object
print(WebReleaseList.to_json())

# convert the object into a dict
web_release_list_dict = web_release_list_instance.to_dict()
# create an instance of WebReleaseList from a dict
web_release_list_from_dict = WebReleaseList.from_dict(web_release_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


