# DtoOhpmTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** |  | [optional] 
**digest** | **str** |  | [optional] 
**last_pusher** | [**DtoLastPusher**](DtoLastPusher.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pull_count** | **int** |  | [optional] 
**recent_pull_count** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_ohpm_tag import DtoOhpmTag

# TODO update the JSON string below
json = "{}"
# create an instance of DtoOhpmTag from a JSON string
dto_ohpm_tag_instance = DtoOhpmTag.from_json(json)
# print the JSON string representation of the object
print(DtoOhpmTag.to_json())

# convert the object into a dict
dto_ohpm_tag_dict = dto_ohpm_tag_instance.to_dict()
# create an instance of DtoOhpmTag from a dict
dto_ohpm_tag_from_dict = DtoOhpmTag.from_dict(dto_ohpm_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


