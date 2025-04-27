# DtoHarborRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the repository | [optional] 
**labels** | **List[str]** | The repository labels | [optional] 
**push_time** | **str** | The push time of the artifact inside the repository Format: date-time | [optional] 
**pusher_id** | **int** | The ID of the pusher who push the artifact. | [optional] 
**recent_pull_count** | **int** | The count that the artifact inside the repository recent pulled | [optional] 

## Example

```python
from cnb_api.models.dto_harbor_repository import DtoHarborRepository

# TODO update the JSON string below
json = "{}"
# create an instance of DtoHarborRepository from a JSON string
dto_harbor_repository_instance = DtoHarborRepository.from_json(json)
# print the JSON string representation of the object
print(DtoHarborRepository.to_json())

# convert the object into a dict
dto_harbor_repository_dict = dto_harbor_repository_instance.to_dict()
# create an instance of DtoHarborRepository from a dict
dto_harbor_repository_from_dict = DtoHarborRepository.from_dict(dto_harbor_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


