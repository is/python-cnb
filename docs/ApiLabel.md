# ApiLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_label import ApiLabel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiLabel from a JSON string
api_label_instance = ApiLabel.from_json(json)
# print the JSON string representation of the object
print(ApiLabel.to_json())

# convert the object into a dict
api_label_dict = api_label_instance.to_dict()
# create an instance of ApiLabel from a dict
api_label_from_dict = ApiLabel.from_dict(api_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


