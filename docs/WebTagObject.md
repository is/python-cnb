# WebTagObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**tagger** | [**WebSignature**](WebSignature.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_tag_object import WebTagObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebTagObject from a JSON string
web_tag_object_instance = WebTagObject.from_json(json)
# print the JSON string representation of the object
print(WebTagObject.to_json())

# convert the object into a dict
web_tag_object_dict = web_tag_object_instance.to_dict()
# create an instance of WebTagObject from a dict
web_tag_object_from_dict = WebTagObject.from_dict(web_tag_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


