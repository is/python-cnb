# LabelOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.label_option import LabelOption

# TODO update the JSON string below
json = "{}"
# create an instance of LabelOption from a JSON string
label_option_instance = LabelOption.from_json(json)
# print the JSON string representation of the object
print(LabelOption.to_json())

# convert the object into a dict
label_option_dict = label_option_instance.to_dict()
# create an instance of LabelOption from a dict
label_option_from_dict = LabelOption.from_dict(label_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


