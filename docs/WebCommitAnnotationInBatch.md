# WebCommitAnnotationInBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[WebCommitAnnotation]**](WebCommitAnnotation.md) |  | [optional] 
**commit_hash** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_commit_annotation_in_batch import WebCommitAnnotationInBatch

# TODO update the JSON string below
json = "{}"
# create an instance of WebCommitAnnotationInBatch from a JSON string
web_commit_annotation_in_batch_instance = WebCommitAnnotationInBatch.from_json(json)
# print the JSON string representation of the object
print(WebCommitAnnotationInBatch.to_json())

# convert the object into a dict
web_commit_annotation_in_batch_dict = web_commit_annotation_in_batch_instance.to_dict()
# create an instance of WebCommitAnnotationInBatch from a dict
web_commit_annotation_in_batch_from_dict = WebCommitAnnotationInBatch.from_dict(web_commit_annotation_in_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


