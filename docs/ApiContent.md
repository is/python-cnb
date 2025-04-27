# ApiContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**entries** | [**List[ApiTreeEntry]**](ApiTreeEntry.md) |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_content import ApiContent

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContent from a JSON string
api_content_instance = ApiContent.from_json(json)
# print the JSON string representation of the object
print(ApiContent.to_json())

# convert the object into a dict
api_content_dict = api_content_instance.to_dict()
# create an instance of ApiContent from a dict
api_content_from_dict = ApiContent.from_dict(api_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


