# IdentityState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nick_name** | **str** |  | [optional] 
**ok** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.identity_state import IdentityState

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityState from a JSON string
identity_state_instance = IdentityState.from_json(json)
# print the JSON string representation of the object
print(IdentityState.to_json())

# convert the object into a dict
identity_state_dict = identity_state_instance.to_dict()
# create an instance of IdentityState from a dict
identity_state_from_dict = IdentityState.from_dict(identity_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


