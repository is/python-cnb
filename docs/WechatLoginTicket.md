# WechatLoginTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.wechat_login_ticket import WechatLoginTicket

# TODO update the JSON string below
json = "{}"
# create an instance of WechatLoginTicket from a JSON string
wechat_login_ticket_instance = WechatLoginTicket.from_json(json)
# print the JSON string representation of the object
print(WechatLoginTicket.to_json())

# convert the object into a dict
wechat_login_ticket_dict = wechat_login_ticket_instance.to_dict()
# create an instance of WechatLoginTicket from a dict
wechat_login_ticket_from_dict = WechatLoginTicket.from_dict(wechat_login_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


