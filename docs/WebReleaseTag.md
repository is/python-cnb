# WebReleaseTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release** | [**WebRelease**](WebRelease.md) |  | [optional] 
**tag** | [**WebTag**](WebTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_release_tag import WebReleaseTag

# TODO update the JSON string below
json = "{}"
# create an instance of WebReleaseTag from a JSON string
web_release_tag_instance = WebReleaseTag.from_json(json)
# print the JSON string representation of the object
print(WebReleaseTag.to_json())

# convert the object into a dict
web_release_tag_dict = web_release_tag_instance.to_dict()
# create an instance of WebReleaseTag from a dict
web_release_tag_from_dict = WebReleaseTag.from_dict(web_release_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


