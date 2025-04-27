# WebLabelOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repo_id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_label_option import WebLabelOption

# TODO update the JSON string below
json = "{}"
# create an instance of WebLabelOption from a JSON string
web_label_option_instance = WebLabelOption.from_json(json)
# print the JSON string representation of the object
print(WebLabelOption.to_json())

# convert the object into a dict
web_label_option_dict = web_label_option_instance.to_dict()
# create an instance of WebLabelOption from a dict
web_label_option_from_dict = WebLabelOption.from_dict(web_label_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


