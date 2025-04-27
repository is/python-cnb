# WebapiPutCommitAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_put_commit_annotation import WebapiPutCommitAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPutCommitAnnotation from a JSON string
webapi_put_commit_annotation_instance = WebapiPutCommitAnnotation.from_json(json)
# print the JSON string representation of the object
print(WebapiPutCommitAnnotation.to_json())

# convert the object into a dict
webapi_put_commit_annotation_dict = webapi_put_commit_annotation_instance.to_dict()
# create an instance of WebapiPutCommitAnnotation from a dict
webapi_put_commit_annotation_from_dict = WebapiPutCommitAnnotation.from_dict(webapi_put_commit_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


