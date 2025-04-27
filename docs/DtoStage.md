# DtoStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | stage 耗时 | [optional] 
**status** | **str** | stage 状态 | [optional] 

## Example

```python
from cnb_api.models.dto_stage import DtoStage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoStage from a JSON string
dto_stage_instance = DtoStage.from_json(json)
# print the JSON string representation of the object
print(DtoStage.to_json())

# convert the object into a dict
dto_stage_dict = dto_stage_instance.to_dict()
# create an instance of DtoStage from a dict
dto_stage_from_dict = DtoStage.from_dict(dto_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


