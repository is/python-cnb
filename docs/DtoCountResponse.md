# DtoCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **int** |  | [optional] 
**repo** | **int** |  | [optional] 
**user** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_count_response import DtoCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCountResponse from a JSON string
dto_count_response_instance = DtoCountResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCountResponse.to_json())

# convert the object into a dict
dto_count_response_dict = dto_count_response_instance.to_dict()
# create an instance of DtoCountResponse from a dict
dto_count_response_from_dict = DtoCountResponse.from_dict(dto_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


