# WebCSDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**var_field** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_cs_detail import WebCSDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WebCSDetail from a JSON string
web_cs_detail_instance = WebCSDetail.from_json(json)
# print the JSON string representation of the object
print(WebCSDetail.to_json())

# convert the object into a dict
web_cs_detail_dict = web_cs_detail_instance.to_dict()
# create an instance of WebCSDetail from a dict
web_cs_detail_from_dict = WebCSDetail.from_dict(web_cs_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


