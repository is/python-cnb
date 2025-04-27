# WebMIMEType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**externsion** | **str** |  | [optional] 
**is_audio** | **bool** |  | [optional] 
**is_browsable_binary_type** | **bool** |  | [optional] 
**is_image** | **bool** |  | [optional] 
**is_pdf** | **bool** |  | [optional] 
**is_representable_as_text** | **bool** |  | [optional] 
**is_svg_image** | **bool** |  | [optional] 
**is_text** | **bool** |  | [optional] 
**is_video** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_mime_type import WebMIMEType

# TODO update the JSON string below
json = "{}"
# create an instance of WebMIMEType from a JSON string
web_mime_type_instance = WebMIMEType.from_json(json)
# print the JSON string representation of the object
print(WebMIMEType.to_json())

# convert the object into a dict
web_mime_type_dict = web_mime_type_instance.to_dict()
# create an instance of WebMIMEType from a dict
web_mime_type_from_dict = WebMIMEType.from_dict(web_mime_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


