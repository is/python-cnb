# HandlerLicenseListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**spdx_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_license_list_item import HandlerLicenseListItem

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerLicenseListItem from a JSON string
handler_license_list_item_instance = HandlerLicenseListItem.from_json(json)
# print the JSON string representation of the object
print(HandlerLicenseListItem.to_json())

# convert the object into a dict
handler_license_list_item_dict = handler_license_list_item_instance.to_dict()
# create an instance of HandlerLicenseListItem from a dict
handler_license_list_item_from_dict = HandlerLicenseListItem.from_dict(handler_license_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


