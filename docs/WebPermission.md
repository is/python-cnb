# WebPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_push_git_tag** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.web_permission import WebPermission

# TODO update the JSON string below
json = "{}"
# create an instance of WebPermission from a JSON string
web_permission_instance = WebPermission.from_json(json)
# print the JSON string representation of the object
print(WebPermission.to_json())

# convert the object into a dict
web_permission_dict = web_permission_instance.to_dict()
# create an instance of WebPermission from a dict
web_permission_from_dict = WebPermission.from_dict(web_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


