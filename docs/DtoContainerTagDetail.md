# DtoContainerTagDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**annotations** | [**DtoContainerAnnotation**](DtoContainerAnnotation.md) |  | [optional] 
**image** | [**DtoContainerImage**](DtoContainerImage.md) |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**options** | [**List[DtoContainerImage]**](DtoContainerImage.md) |  | [optional] 
**package** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_container_tag_detail import DtoContainerTagDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoContainerTagDetail from a JSON string
dto_container_tag_detail_instance = DtoContainerTagDetail.from_json(json)
# print the JSON string representation of the object
print(DtoContainerTagDetail.to_json())

# convert the object into a dict
dto_container_tag_detail_dict = dto_container_tag_detail_instance.to_dict()
# create an instance of DtoContainerTagDetail from a dict
dto_container_tag_detail_from_dict = DtoContainerTagDetail.from_dict(dto_container_tag_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


