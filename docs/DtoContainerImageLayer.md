# DtoContainerImageLayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_image_layer import DtoContainerImageLayer

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerImageLayer from a JSON string
dto_container_image_layer_instance = DtoContainerImageLayer.from_json(json)
# print the JSON string representation of the object
print(DtoContainerImageLayer.to_json())

# convert the object into a dict
dto_container_image_layer_dict = dto_container_image_layer_instance.to_dict()
# create an instance of DtoContainerImageLayer from a dict
dto_container_image_layer_from_dict = DtoContainerImageLayer.from_dict(dto_container_image_layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


