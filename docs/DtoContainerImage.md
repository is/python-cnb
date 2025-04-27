# DtoContainerImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**digest** | **str** |  | [optional] 
**layers** | [**List[DtoContainerImageLayer]**](DtoContainerImageLayer.md) |  | [optional] 
**os** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_image import DtoContainerImage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerImage from a JSON string
dto_container_image_instance = DtoContainerImage.from_json(json)
# print the JSON string representation of the object
print(DtoContainerImage.to_json())

# convert the object into a dict
dto_container_image_dict = dto_container_image_instance.to_dict()
# create an instance of DtoContainerImage from a dict
dto_container_image_from_dict = DtoContainerImage.from_dict(dto_container_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


