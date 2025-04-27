# WebTagList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_count** | **int** |  | [optional] 
**tag_count** | **int** |  | [optional] 
**tags** | [**List[WebTag]**](WebTag.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_tag_list import WebTagList

# TODO update the JSON string below
json = "{}"
# create an instance of WebTagList from a JSON string
web_tag_list_instance = WebTagList.from_json(json)
# print the JSON string representation of the object
print(WebTagList.to_json())

# convert the object into a dict
web_tag_list_dict = web_tag_list_instance.to_dict()
# create an instance of WebTagList from a dict
web_tag_list_from_dict = WebTagList.from_dict(web_tag_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


