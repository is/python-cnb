# WebBranchListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ahead** | **int** |  | [optional] 
**associated_pull_request** | [**WebBranchPullRequest**](WebBranchPullRequest.md) |  | [optional] 
**behind** | **int** |  | [optional] 
**commit** | [**WebCommit**](WebCommit.md) |  | [optional] 
**dev_meta** | **List[int]** |  | [optional] 
**is_head** | **bool** |  | [optional] 
**is_protected** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_branch_list_item import WebBranchListItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebBranchListItem from a JSON string
web_branch_list_item_instance = WebBranchListItem.from_json(json)
# print the JSON string representation of the object
print(WebBranchListItem.to_json())

# convert the object into a dict
web_branch_list_item_dict = web_branch_list_item_instance.to_dict()
# create an instance of WebBranchListItem from a dict
web_branch_list_item_from_dict = WebBranchListItem.from_dict(web_branch_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


