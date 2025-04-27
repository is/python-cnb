# DtoInvitationWithEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**creator** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_match** | **bool** |  | [optional] 
**expire** | **int** |  | [optional] 
**is_outside_collaborator** | **bool** |  | [optional] 
**resource** | [**DtoResources**](DtoResources.md) |  | [optional] 
**role** | [**ConstantAccessRole**](ConstantAccessRole.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_invitation_with_email import DtoInvitationWithEmail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoInvitationWithEmail from a JSON string
dto_invitation_with_email_instance = DtoInvitationWithEmail.from_json(json)
# print the JSON string representation of the object
print(DtoInvitationWithEmail.to_json())

# convert the object into a dict
dto_invitation_with_email_dict = dto_invitation_with_email_instance.to_dict()
# create an instance of DtoInvitationWithEmail from a dict
dto_invitation_with_email_from_dict = DtoInvitationWithEmail.from_dict(dto_invitation_with_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


