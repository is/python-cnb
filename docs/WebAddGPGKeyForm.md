# WebAddGPGKeyForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**armored_public_key** | **str** | A GPG public key in ASCII-armored format. | [optional] 
**name** | **str** | A descriptive name for the new key. | [optional] 

## Example

```python
from cnb_api.models.web_add_gpg_key_form import WebAddGPGKeyForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebAddGPGKeyForm from a JSON string
web_add_gpg_key_form_instance = WebAddGPGKeyForm.from_json(json)
# print the JSON string representation of the object
print(WebAddGPGKeyForm.to_json())

# convert the object into a dict
web_add_gpg_key_form_dict = web_add_gpg_key_form_instance.to_dict()
# create an instance of WebAddGPGKeyForm from a dict
web_add_gpg_key_form_from_dict = WebAddGPGKeyForm.from_dict(web_add_gpg_key_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


