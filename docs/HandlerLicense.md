# HandlerLicense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**conditions** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**limitations** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**spdx_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_license import HandlerLicense

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerLicense from a JSON string
handler_license_instance = HandlerLicense.from_json(json)
# print the JSON string representation of the object
print(HandlerLicense.to_json())

# convert the object into a dict
handler_license_dict = handler_license_instance.to_dict()
# create an instance of HandlerLicense from a dict
handler_license_from_dict = HandlerLicense.from_dict(handler_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


