# DtoBoolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.dto_bool_response import DtoBoolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBoolResponse from a JSON string
dto_bool_response_instance = DtoBoolResponse.from_json(json)
# print the JSON string representation of the object
print(DtoBoolResponse.to_json())

# convert the object into a dict
dto_bool_response_dict = dto_bool_response_instance.to_dict()
# create an instance of DtoBoolResponse from a dict
dto_bool_response_from_dict = DtoBoolResponse.from_dict(dto_bool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


