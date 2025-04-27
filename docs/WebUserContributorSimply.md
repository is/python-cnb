# WebUserContributorSimply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_count** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_user_contributor_simply import WebUserContributorSimply

# TODO update the JSON string below
json = "{}"
# create an instance of WebUserContributorSimply from a JSON string
web_user_contributor_simply_instance = WebUserContributorSimply.from_json(json)
# print the JSON string representation of the object
print(WebUserContributorSimply.to_json())

# convert the object into a dict
web_user_contributor_simply_dict = web_user_contributor_simply_instance.to_dict()
# create an instance of WebUserContributorSimply from a dict
web_user_contributor_simply_from_dict = WebUserContributorSimply.from_dict(web_user_contributor_simply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


