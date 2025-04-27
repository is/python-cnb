# WebGPGEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | 邮箱 | [optional] 
**verified** | **bool** | 是否已验证 | [optional] 

## Example

```python
from cnb_api.models.web_gpg_email import WebGPGEmail

# TODO update the JSON string below
json = "{}"
# create an instance of WebGPGEmail from a JSON string
web_gpg_email_instance = WebGPGEmail.from_json(json)
# print the JSON string representation of the object
print(WebGPGEmail.to_json())

# convert the object into a dict
web_gpg_email_dict = web_gpg_email_instance.to_dict()
# create an instance of WebGPGEmail from a dict
web_gpg_email_from_dict = WebGPGEmail.from_dict(web_gpg_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


