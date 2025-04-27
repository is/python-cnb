# WechatAuthorizedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_max_day** | **int** | 默认的过期天数 | [optional] 
**freeze** | **bool** |  | [optional] 
**head_img_url** | **str** |  | [optional] 
**max_days_options** | **List[int]** | 用户登陆过期天数可选项 | [optional] 
**nick_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.wechat_authorized_user import WechatAuthorizedUser

# TODO update the JSON string below
json = "{}"
# create an instance of WechatAuthorizedUser from a JSON string
wechat_authorized_user_instance = WechatAuthorizedUser.from_json(json)
# print the JSON string representation of the object
print(WechatAuthorizedUser.to_json())

# convert the object into a dict
wechat_authorized_user_dict = wechat_authorized_user_instance.to_dict()
# create an instance of WechatAuthorizedUser from a dict
wechat_authorized_user_from_dict = WechatAuthorizedUser.from_dict(wechat_authorized_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


