# ApiSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_signature import ApiSignature

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSignature from a JSON string
api_signature_instance = ApiSignature.from_json(json)
# print the JSON string representation of the object
print(ApiSignature.to_json())

# convert the object into a dict
api_signature_dict = api_signature_instance.to_dict()
# create an instance of ApiSignature from a dict
api_signature_from_dict = ApiSignature.from_dict(api_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


