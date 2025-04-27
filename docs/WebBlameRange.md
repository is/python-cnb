# WebBlameRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**ending_line** | **int** |  | [optional] 
**starting_line** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_blame_range import WebBlameRange

# TODO update the JSON string below
json = "{}"
# create an instance of WebBlameRange from a JSON string
web_blame_range_instance = WebBlameRange.from_json(json)
# print the JSON string representation of the object
print(WebBlameRange.to_json())

# convert the object into a dict
web_blame_range_dict = web_blame_range_instance.to_dict()
# create an instance of WebBlameRange from a dict
web_blame_range_from_dict = WebBlameRange.from_dict(web_blame_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


