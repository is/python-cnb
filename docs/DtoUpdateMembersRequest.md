# DtoUpdateMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | **str** |  | [optional] 
**is_outside_collaborator** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateMembersRequest from a JSON string
dto_update_members_request_instance = DtoUpdateMembersRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateMembersRequest.to_json())

# convert the object into a dict
dto_update_members_request_dict = dto_update_members_request_instance.to_dict()
# create an instance of DtoUpdateMembersRequest from a dict
dto_update_members_request_from_dict = DtoUpdateMembersRequest.from_dict(dto_update_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


