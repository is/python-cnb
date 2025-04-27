# WebSubEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_sub_entry import WebSubEntry

# TODO update the JSON string below
json = "{}"
# create an instance of WebSubEntry from a JSON string
web_sub_entry_instance = WebSubEntry.from_json(json)
# print the JSON string representation of the object
print(WebSubEntry.to_json())

# convert the object into a dict
web_sub_entry_dict = web_sub_entry_instance.to_dict()
# create an instance of WebSubEntry from a dict
web_sub_entry_from_dict = WebSubEntry.from_dict(web_sub_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


