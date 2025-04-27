# HttpUpdateUserInfoPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**wechat_mp** | **str** |  | [optional] 
**wechat_mp_qrcode** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.http_update_user_info_payload import HttpUpdateUserInfoPayload

# TODO update the JSON string below
json = "{}"
# create an instance of HttpUpdateUserInfoPayload from a JSON string
http_update_user_info_payload_instance = HttpUpdateUserInfoPayload.from_json(json)
# print the JSON string representation of the object
print(HttpUpdateUserInfoPayload.to_json())

# convert the object into a dict
http_update_user_info_payload_dict = http_update_user_info_payload_instance.to_dict()
# create an instance of HttpUpdateUserInfoPayload from a dict
http_update_user_info_payload_from_dict = HttpUpdateUserInfoPayload.from_dict(http_update_user_info_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


