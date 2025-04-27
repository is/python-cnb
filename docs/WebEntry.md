# WebEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[WebSubEntry]**](WebSubEntry.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_entry import WebEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebEntry from a JSON string
web_entry_instance = WebEntry.from_json(json)
# print the JSON string representation of the object
print(WebEntry.to_json())

# convert the object into a dict
web_entry_dict = web_entry_instance.to_dict()
# create an instance of WebEntry from a dict
web_entry_from_dict = WebEntry.from_dict(web_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


