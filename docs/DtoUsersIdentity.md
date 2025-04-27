# DtoUsersIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_users_identity import DtoUsersIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsersIdentity from a JSON string
dto_users_identity_instance = DtoUsersIdentity.from_json(json)
# print the JSON string representation of the object
print(DtoUsersIdentity.to_json())

# convert the object into a dict
dto_users_identity_dict = dto_users_identity_instance.to_dict()
# create an instance of DtoUsersIdentity from a dict
dto_users_identity_from_dict = DtoUsersIdentity.from_dict(dto_users_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


