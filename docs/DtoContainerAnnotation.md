# DtoContainerAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_annotation import DtoContainerAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerAnnotation from a JSON string
dto_container_annotation_instance = DtoContainerAnnotation.from_json(json)
# print the JSON string representation of the object
print(DtoContainerAnnotation.to_json())

# convert the object into a dict
dto_container_annotation_dict = dto_container_annotation_instance.to_dict()
# create an instance of DtoContainerAnnotation from a dict
dto_container_annotation_from_dict = DtoContainerAnnotation.from_dict(dto_container_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


