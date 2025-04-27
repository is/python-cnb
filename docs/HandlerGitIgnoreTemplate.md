# HandlerGitIgnoreTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.handler_git_ignore_template import HandlerGitIgnoreTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of HandlerGitIgnoreTemplate from a JSON string
handler_git_ignore_template_instance = HandlerGitIgnoreTemplate.from_json(json)
# print the JSON string representation of the object
print(HandlerGitIgnoreTemplate.to_json())

# convert the object into a dict
handler_git_ignore_template_dict = handler_git_ignore_template_instance.to_dict()
# create an instance of HandlerGitIgnoreTemplate from a dict
handler_git_ignore_template_from_dict = HandlerGitIgnoreTemplate.from_dict(handler_git_ignore_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


