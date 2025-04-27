# WebIssueResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | [**List[GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo]**](GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo.md) |  | [optional] 
**author** | [**GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo**](GitWoaComCnbMonorepoMissionMissionResourceDtoWebUserInfo.md) |  | [optional] 
**comment_count** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**customer_fields** | [**List[WebCustomerField]**](WebCustomerField.md) |  | [optional] 
**ended_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**labels** | [**List[WebLabelOption]**](WebLabelOption.md) |  | [optional] 
**number** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**repo_slug** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_reason** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_resource import WebIssueResource

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueResource from a JSON string
web_issue_resource_instance = WebIssueResource.from_json(json)
# print the JSON string representation of the object
print(WebIssueResource.to_json())

# convert the object into a dict
web_issue_resource_dict = web_issue_resource_instance.to_dict()
# create an instance of WebIssueResource from a dict
web_issue_resource_from_dict = WebIssueResource.from_dict(web_issue_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


