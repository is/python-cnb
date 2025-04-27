# DtoWxJsSdkSign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **str** |  | [optional] 
**noncestr** | **str** |  | [optional] 
**sign** | **str** | 签名结果 | [optional] 
**timestamp** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_wx_js_sdk_sign import DtoWxJsSdkSign

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWxJsSdkSign from a JSON string
dto_wx_js_sdk_sign_instance = DtoWxJsSdkSign.from_json(json)
# print the JSON string representation of the object
print(DtoWxJsSdkSign.to_json())

# convert the object into a dict
dto_wx_js_sdk_sign_dict = dto_wx_js_sdk_sign_instance.to_dict()
# create an instance of DtoWxJsSdkSign from a dict
dto_wx_js_sdk_sign_from_dict = DtoWxJsSdkSign.from_dict(dto_wx_js_sdk_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


