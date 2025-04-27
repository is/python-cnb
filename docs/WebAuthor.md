# WebAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_author import WebAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthor from a JSON string
web_author_instance = WebAuthor.from_json(json)
# print the JSON string representation of the object
print(WebAuthor.to_json())

# convert the object into a dict
web_author_dict = web_author_instance.to_dict()
# create an instance of WebAuthor from a dict
web_author_from_dict = WebAuthor.from_dict(web_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


