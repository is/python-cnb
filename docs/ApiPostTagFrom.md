# ApiPostTagFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_post_tag_from import ApiPostTagFrom

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostTagFrom from a JSON string
api_post_tag_from_instance = ApiPostTagFrom.from_json(json)
# print the JSON string representation of the object
print(ApiPostTagFrom.to_json())

# convert the object into a dict
api_post_tag_from_dict = api_post_tag_from_instance.to_dict()
# create an instance of ApiPostTagFrom from a dict
api_post_tag_from_from_dict = ApiPostTagFrom.from_dict(api_post_tag_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


