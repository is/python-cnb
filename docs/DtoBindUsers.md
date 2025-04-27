# DtoBindUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**openid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_bind_users import DtoBindUsers

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBindUsers from a JSON string
dto_bind_users_instance = DtoBindUsers.from_json(json)
# print the JSON string representation of the object
print(DtoBindUsers.to_json())

# convert the object into a dict
dto_bind_users_dict = dto_bind_users_instance.to_dict()
# create an instance of DtoBindUsers from a dict
dto_bind_users_from_dict = DtoBindUsers.from_dict(dto_bind_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


