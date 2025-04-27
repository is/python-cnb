# WebCommitAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**meta** | **Dict[str, object]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_annotation import WebCommitAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitAnnotation from a JSON string
web_commit_annotation_instance = WebCommitAnnotation.from_json(json)
# print the JSON string representation of the object
print(WebCommitAnnotation.to_json())

# convert the object into a dict
web_commit_annotation_dict = web_commit_annotation_instance.to_dict()
# create an instance of WebCommitAnnotation from a dict
web_commit_annotation_from_dict = WebCommitAnnotation.from_dict(web_commit_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


