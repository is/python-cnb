# DtoUsersLangPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_users_lang_payload import DtoUsersLangPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsersLangPayload from a JSON string
dto_users_lang_payload_instance = DtoUsersLangPayload.from_json(json)
# print the JSON string representation of the object
print(DtoUsersLangPayload.to_json())

# convert the object into a dict
dto_users_lang_payload_dict = dto_users_lang_payload_instance.to_dict()
# create an instance of DtoUsersLangPayload from a dict
dto_users_lang_payload_from_dict = DtoUsersLangPayload.from_dict(dto_users_lang_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


