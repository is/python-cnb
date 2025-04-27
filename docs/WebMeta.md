# WebMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gen_branch** | **str** |  | [optional] 
**gen_hash** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_meta import WebMeta

# TODO update the JSON string below
json = "{}"
# create an instance of WebMeta from a JSON string
web_meta_instance = WebMeta.from_json(json)
# print the JSON string representation of the object
print(WebMeta.to_json())

# convert the object into a dict
web_meta_dict = web_meta_instance.to_dict()
# create an instance of WebMeta from a dict
web_meta_from_dict = WebMeta.from_dict(web_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


