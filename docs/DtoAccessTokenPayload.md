# DtoAccessTokenPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**expired_at** | [**ConvertNullTime**](ConvertNullTime.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_access_token_payload import DtoAccessTokenPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAccessTokenPayload from a JSON string
dto_access_token_payload_instance = DtoAccessTokenPayload.from_json(json)
# print the JSON string representation of the object
print(DtoAccessTokenPayload.to_json())

# convert the object into a dict
dto_access_token_payload_dict = dto_access_token_payload_instance.to_dict()
# create an instance of DtoAccessTokenPayload from a dict
dto_access_token_payload_from_dict = DtoAccessTokenPayload.from_dict(dto_access_token_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


