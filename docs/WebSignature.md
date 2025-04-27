# WebSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_signature import WebSignature

# TODO update the JSON string below
json = "{}"
# create an instance of WebSignature from a JSON string
web_signature_instance = WebSignature.from_json(json)
# print the JSON string representation of the object
print(WebSignature.to_json())

# convert the object into a dict
web_signature_dict = web_signature_instance.to_dict()
# create an instance of WebSignature from a dict
web_signature_from_dict = WebSignature.from_dict(web_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


