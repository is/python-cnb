# WebRepoContribSimply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**WebMeta**](WebMeta.md) |  | [optional] 
**top_100_contrib** | [**List[WebUserContributorSimply]**](WebUserContributorSimply.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_repo_contrib_simply import WebRepoContribSimply

# TODO update the JSON string below
json = "{}"
# create an instance of WebRepoContribSimply from a JSON string
web_repo_contrib_simply_instance = WebRepoContribSimply.from_json(json)
# print the JSON string representation of the object
print(WebRepoContribSimply.to_json())

# convert the object into a dict
web_repo_contrib_simply_dict = web_repo_contrib_simply_instance.to_dict()
# create an instance of WebRepoContribSimply from a dict
web_repo_contrib_simply_from_dict = WebRepoContribSimply.from_dict(web_repo_contrib_simply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


