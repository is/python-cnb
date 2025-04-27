# OpenapiHeadRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.openapi_head_ref import OpenapiHeadRef

# TODO update the JSON string below
json = "{}"
# create an instance of OpenapiHeadRef from a JSON string
openapi_head_ref_instance = OpenapiHeadRef.from_json(json)
# print the JSON string representation of the object
print(OpenapiHeadRef.to_json())

# convert the object into a dict
openapi_head_ref_dict = openapi_head_ref_instance.to_dict()
# create an instance of OpenapiHeadRef from a dict
openapi_head_ref_from_dict = OpenapiHeadRef.from_dict(openapi_head_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


