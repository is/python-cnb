# DtoWorkspacePageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_workspace_page_info import DtoWorkspacePageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWorkspacePageInfo from a JSON string
dto_workspace_page_info_instance = DtoWorkspacePageInfo.from_json(json)
# print the JSON string representation of the object
print(DtoWorkspacePageInfo.to_json())

# convert the object into a dict
dto_workspace_page_info_dict = dto_workspace_page_info_instance.to_dict()
# create an instance of DtoWorkspacePageInfo from a dict
dto_workspace_page_info_from_dict = DtoWorkspacePageInfo.from_dict(dto_workspace_page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


