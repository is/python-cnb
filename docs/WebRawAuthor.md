# WebRawAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_email** | **str** |  | [optional] 
**author_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_raw_author import WebRawAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of WebRawAuthor from a JSON string
web_raw_author_instance = WebRawAuthor.from_json(json)
# print the JSON string representation of the object
print(WebRawAuthor.to_json())

# convert the object into a dict
web_raw_author_dict = web_raw_author_instance.to_dict()
# create an instance of WebRawAuthor from a dict
web_raw_author_from_dict = WebRawAuthor.from_dict(web_raw_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


