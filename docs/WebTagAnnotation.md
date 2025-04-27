# WebTagAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_tag_annotation import WebTagAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of WebTagAnnotation from a JSON string
web_tag_annotation_instance = WebTagAnnotation.from_json(json)
# print the JSON string representation of the object
print(WebTagAnnotation.to_json())

# convert the object into a dict
web_tag_annotation_dict = web_tag_annotation_instance.to_dict()
# create an instance of WebTagAnnotation from a dict
web_tag_annotation_from_dict = WebTagAnnotation.from_dict(web_tag_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


