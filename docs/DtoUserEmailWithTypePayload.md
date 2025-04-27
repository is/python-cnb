# DtoUserEmailWithTypePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**type** | [**DtoUserEmailType**](DtoUserEmailType.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_user_email_with_type_payload import DtoUserEmailWithTypePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserEmailWithTypePayload from a JSON string
dto_user_email_with_type_payload_instance = DtoUserEmailWithTypePayload.from_json(json)
# print the JSON string representation of the object
print(DtoUserEmailWithTypePayload.to_json())

# convert the object into a dict
dto_user_email_with_type_payload_dict = dto_user_email_with_type_payload_instance.to_dict()
# create an instance of DtoUserEmailWithTypePayload from a dict
dto_user_email_with_type_payload_from_dict = DtoUserEmailWithTypePayload.from_dict(dto_user_email_with_type_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


