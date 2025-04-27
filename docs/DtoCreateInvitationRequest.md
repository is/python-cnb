# DtoCreateInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_outside_collaborator** | **bool** |  | [optional] 
**member_number** | **int** |  | [optional] 
**member_role** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**validity_hour** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_create_invitation_request import DtoCreateInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateInvitationRequest from a JSON string
dto_create_invitation_request_instance = DtoCreateInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateInvitationRequest.to_json())

# convert the object into a dict
dto_create_invitation_request_dict = dto_create_invitation_request_instance.to_dict()
# create an instance of DtoCreateInvitationRequest from a dict
dto_create_invitation_request_from_dict = DtoCreateInvitationRequest.from_dict(dto_create_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


