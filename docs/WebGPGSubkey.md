# WebGPGSubkey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | 子密钥系统创建时间（添加到系统时间） | [optional] 
**expired_at** | **str** | 子密钥过期时间 | [optional] 
**fingerprint** | **str** | 子密钥指纹 | [optional] 
**id** | **str** |  | [optional] 
**key_creation_time** | **str** | 子密钥创建时间 | [optional] 
**key_id** | **str** | 子密钥 KeyID | [optional] 
**primary_key_id** | **str** | 主密钥 KeyID | [optional] 

## Example

```python
from cnb_api.models.web_gpg_subkey import WebGPGSubkey

# TODO update the JSON string below
json = "{}"
# create an instance of WebGPGSubkey from a JSON string
web_gpg_subkey_instance = WebGPGSubkey.from_json(json)
# print the JSON string representation of the object
print(WebGPGSubkey.to_json())

# convert the object into a dict
web_gpg_subkey_dict = web_gpg_subkey_instance.to_dict()
# create an instance of WebGPGSubkey from a dict
web_gpg_subkey_from_dict = WebGPGSubkey.from_dict(web_gpg_subkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


