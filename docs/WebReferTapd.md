# WebReferTapd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**due** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**view_link** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_refer_tapd import WebReferTapd

# TODO update the JSON string below
json = "{}"
# create an instance of WebReferTapd from a JSON string
web_refer_tapd_instance = WebReferTapd.from_json(json)
# print the JSON string representation of the object
print(WebReferTapd.to_json())

# convert the object into a dict
web_refer_tapd_dict = web_refer_tapd_instance.to_dict()
# create an instance of WebReferTapd from a dict
web_refer_tapd_from_dict = WebReferTapd.from_dict(web_refer_tapd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


