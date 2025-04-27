# DtoHandoverMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **str** |  | [optional] 
**before** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_handover_member_request import DtoHandoverMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoHandoverMemberRequest from a JSON string
dto_handover_member_request_instance = DtoHandoverMemberRequest.from_json(json)
# print the JSON string representation of the object
print(DtoHandoverMemberRequest.to_json())

# convert the object into a dict
dto_handover_member_request_dict = dto_handover_member_request_instance.to_dict()
# create an instance of DtoHandoverMemberRequest from a dict
dto_handover_member_request_from_dict = DtoHandoverMemberRequest.from_dict(dto_handover_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


