# DtoUserEmailPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_user_email_payload import DtoUserEmailPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserEmailPayload from a JSON string
dto_user_email_payload_instance = DtoUserEmailPayload.from_json(json)
# print the JSON string representation of the object
print(DtoUserEmailPayload.to_json())

# convert the object into a dict
dto_user_email_payload_dict = dto_user_email_payload_instance.to_dict()
# create an instance of DtoUserEmailPayload from a dict
dto_user_email_payload_from_dict = DtoUserEmailPayload.from_dict(dto_user_email_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


