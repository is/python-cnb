# WebTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**has_release** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**tag_object** | [**WebTagObject**](WebTagObject.md) |  | [optional] 
**tagger** | [**GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo**](GitWoaComCnbMonorepoGitInternalAppGitServiceBffWebUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_tag import WebTag

# TODO update the JSON string below
json = "{}"
# create an instance of WebTag from a JSON string
web_tag_instance = WebTag.from_json(json)
# print the JSON string representation of the object
print(WebTag.to_json())

# convert the object into a dict
web_tag_dict = web_tag_instance.to_dict()
# create an instance of WebTag from a dict
web_tag_from_dict = WebTag.from_dict(web_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


