# DtoSearchResponseAny


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**ConstantSearchResourceType**](ConstantSearchResourceType.md) |  | [optional] 
**results** | **object** |  | [optional] 

## Example

```python
from cnb_api.models.dto_search_response_any import DtoSearchResponseAny

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSearchResponseAny from a JSON string
dto_search_response_any_instance = DtoSearchResponseAny.from_json(json)
# print the JSON string representation of the object
print(DtoSearchResponseAny.to_json())

# convert the object into a dict
dto_search_response_any_dict = dto_search_response_any_instance.to_dict()
# create an instance of DtoSearchResponseAny from a dict
dto_search_response_any_from_dict = DtoSearchResponseAny.from_dict(dto_search_response_any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


