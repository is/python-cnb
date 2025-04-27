# DtoLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_label import DtoLabel

# TODO update the JSON string below
json = "{}"
# create an instance of DtoLabel from a JSON string
dto_label_instance = DtoLabel.from_json(json)
# print the JSON string representation of the object
print(DtoLabel.to_json())

# convert the object into a dict
dto_label_dict = dto_label_instance.to_dict()
# create an instance of DtoLabel from a dict
dto_label_from_dict = DtoLabel.from_dict(dto_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


