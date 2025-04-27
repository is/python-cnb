# DtoSyncUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.dto_sync_user_data import DtoSyncUserData

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSyncUserData from a JSON string
dto_sync_user_data_instance = DtoSyncUserData.from_json(json)
# print the JSON string representation of the object
print(DtoSyncUserData.to_json())

# convert the object into a dict
dto_sync_user_data_dict = dto_sync_user_data_instance.to_dict()
# create an instance of DtoSyncUserData from a dict
dto_sync_user_data_from_dict = DtoSyncUserData.from_dict(dto_sync_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


