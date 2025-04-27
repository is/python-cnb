# DtoUserEmailWithCodePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_user_email_with_code_payload import DtoUserEmailWithCodePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserEmailWithCodePayload from a JSON string
dto_user_email_with_code_payload_instance = DtoUserEmailWithCodePayload.from_json(json)
# print the JSON string representation of the object
print(DtoUserEmailWithCodePayload.to_json())

# convert the object into a dict
dto_user_email_with_code_payload_dict = dto_user_email_with_code_payload_instance.to_dict()
# create an instance of DtoUserEmailWithCodePayload from a dict
dto_user_email_with_code_payload_from_dict = DtoUserEmailWithCodePayload.from_dict(dto_user_email_with_code_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


