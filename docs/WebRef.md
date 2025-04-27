# WebRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_head** | **bool** |  | [optional] 
**is_protected** | **bool** |  | [optional] 
**ref** | **str** |  | [optional] 
**target_date** | **str** |  | [optional] 
**target_hash** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_ref import WebRef

# TODO update the JSON string below
json = "{}"
# create an instance of WebRef from a JSON string
web_ref_instance = WebRef.from_json(json)
# print the JSON string representation of the object
print(WebRef.to_json())

# convert the object into a dict
web_ref_dict = web_ref_instance.to_dict()
# create an instance of WebRef from a dict
web_ref_from_dict = WebRef.from_dict(web_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


