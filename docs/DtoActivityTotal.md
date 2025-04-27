# DtoActivityTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ConstantActivityType**](ConstantActivityType.md) |  | [optional] 
**unread** | **bool** |  | [optional] 
**users** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_total import DtoActivityTotal

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityTotal from a JSON string
dto_activity_total_instance = DtoActivityTotal.from_json(json)
# print the JSON string representation of the object
print(DtoActivityTotal.to_json())

# convert the object into a dict
dto_activity_total_dict = dto_activity_total_instance.to_dict()
# create an instance of DtoActivityTotal from a dict
dto_activity_total_from_dict = DtoActivityTotal.from_dict(dto_activity_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


