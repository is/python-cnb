# DtoCreateInvitationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**resource_type** | [**ConstantSlugType**](ConstantSlugType.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_create_invitation_response import DtoCreateInvitationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateInvitationResponse from a JSON string
dto_create_invitation_response_instance = DtoCreateInvitationResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCreateInvitationResponse.to_json())

# convert the object into a dict
dto_create_invitation_response_dict = dto_create_invitation_response_instance.to_dict()
# create an instance of DtoCreateInvitationResponse from a dict
dto_create_invitation_response_from_dict = DtoCreateInvitationResponse.from_dict(dto_create_invitation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


