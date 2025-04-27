# WebBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**is_protected** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_branch import WebBranch

# TODO update the JSON string below
json = "{}"
# create an instance of WebBranch from a JSON string
web_branch_instance = WebBranch.from_json(json)
# print the JSON string representation of the object
print(WebBranch.to_json())

# convert the object into a dict
web_branch_dict = web_branch_instance.to_dict()
# create an instance of WebBranch from a dict
web_branch_from_dict = WebBranch.from_dict(web_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


