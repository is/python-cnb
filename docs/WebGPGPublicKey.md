# WebGPGPublicKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**emails** | [**List[WebGPGEmail]**](WebGPGEmail.md) |  | [optional] 
**expired_at** | **str** | 过期时间 | [optional] 
**fingerprint** | **str** | 公钥指纹 | [optional] 
**id** | **str** |  | [optional] 
**key_creation_time** | **str** | 密钥创建时间 | [optional] 
**key_id** | **str** | 公钥 ID | [optional] 
**name** | **str** | 标题 | [optional] 
**public_key** | **str** |  | [optional] 
**subkeys** | [**List[WebGPGSubkey]**](WebGPGSubkey.md) | 子密钥指纹，当为 primary key 时与 primary_fingerprint 相同 | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_gpg_public_key import WebGPGPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of WebGPGPublicKey from a JSON string
web_gpg_public_key_instance = WebGPGPublicKey.from_json(json)
# print the JSON string representation of the object
print(WebGPGPublicKey.to_json())

# convert the object into a dict
web_gpg_public_key_dict = web_gpg_public_key_instance.to_dict()
# create an instance of WebGPGPublicKey from a dict
web_gpg_public_key_from_dict = WebGPGPublicKey.from_dict(web_gpg_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


