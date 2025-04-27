# DtoContainerTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**annotations** | [**DtoContainerAnnotation**](DtoContainerAnnotation.md) |  | [optional] 
**images** | [**List[DtoContainerImage]**](DtoContainerImage.md) |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_tag import DtoContainerTag

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerTag from a JSON string
dto_container_tag_instance = DtoContainerTag.from_json(json)
# print the JSON string representation of the object
print(DtoContainerTag.to_json())

# convert the object into a dict
dto_container_tag_dict = dto_container_tag_instance.to_dict()
# create an instance of DtoContainerTag from a dict
dto_container_tag_from_dict = DtoContainerTag.from_dict(dto_container_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


