# WebBlames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size** | **int** |  | [optional] 
**file_size_exceeded** | **bool** |  | [optional] 
**file_size_limit** | **int** |  | [optional] 
**ranges** | [**List[WebBlameRange]**](WebBlameRange.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_blames import WebBlames

# TODO update the JSON string below
json = "{}"
# create an instance of WebBlames from a JSON string
web_blames_instance = WebBlames.from_json(json)
# print the JSON string representation of the object
print(WebBlames.to_json())

# convert the object into a dict
web_blames_dict = web_blames_instance.to_dict()
# create an instance of WebBlames from a dict
web_blames_from_dict = WebBlames.from_dict(web_blames_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


