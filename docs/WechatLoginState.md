# WechatLoginState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** |  | [optional] 
**confirmed** | **bool** |  | [optional] 
**is_expired** | **bool** |  | [optional] 
**nick_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.wechat_login_state import WechatLoginState

# TODO update the JSON string below
json = "{}"
# create an instance of WechatLoginState from a JSON string
wechat_login_state_instance = WechatLoginState.from_json(json)
# print the JSON string representation of the object
print(WechatLoginState.to_json())

# convert the object into a dict
wechat_login_state_dict = wechat_login_state_instance.to_dict()
# create an instance of WechatLoginState from a dict
wechat_login_state_from_dict = WechatLoginState.from_dict(wechat_login_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


