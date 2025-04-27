# WebFieldInfoStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | **Dict[str, str]** |  | [optional] 

## Example

```python
from cnb_api.models.web_field_info_status import WebFieldInfoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebFieldInfoStatus from a JSON string
web_field_info_status_instance = WebFieldInfoStatus.from_json(json)
# print the JSON string representation of the object
print(WebFieldInfoStatus.to_json())

# convert the object into a dict
web_field_info_status_dict = web_field_info_status_instance.to_dict()
# create an instance of WebFieldInfoStatus from a dict
web_field_info_status_from_dict = WebFieldInfoStatus.from_dict(web_field_info_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


