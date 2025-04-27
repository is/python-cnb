# WebOverviewBranches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_branches** | [**List[WebBranchListItem]**](WebBranchListItem.md) |  | [optional] 
**default_branch** | [**WebBranchListItem**](WebBranchListItem.md) |  | [optional] 
**has_more_active_branch** | **bool** |  | [optional] 
**has_more_stale_branch** | **bool** |  | [optional] 
**has_more_yours_branch** | **bool** |  | [optional] 
**initialized** | **bool** |  | [optional] 
**stale_branches** | [**List[WebBranchListItem]**](WebBranchListItem.md) |  | [optional] 
**yours_branches** | [**List[WebBranchListItem]**](WebBranchListItem.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_overview_branches import WebOverviewBranches

# TODO update the JSON string below
json = "{}"
# create an instance of WebOverviewBranches from a JSON string
web_overview_branches_instance = WebOverviewBranches.from_json(json)
# print the JSON string representation of the object
print(WebOverviewBranches.to_json())

# convert the object into a dict
web_overview_branches_dict = web_overview_branches_instance.to_dict()
# create an instance of WebOverviewBranches from a dict
web_overview_branches_from_dict = WebOverviewBranches.from_dict(web_overview_branches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


