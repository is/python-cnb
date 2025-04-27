# IdentityTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.identity_ticket import IdentityTicket

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityTicket from a JSON string
identity_ticket_instance = IdentityTicket.from_json(json)
# print the JSON string representation of the object
print(IdentityTicket.to_json())

# convert the object into a dict
identity_ticket_dict = identity_ticket_instance.to_dict()
# create an instance of IdentityTicket from a dict
identity_ticket_from_dict = IdentityTicket.from_dict(identity_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


