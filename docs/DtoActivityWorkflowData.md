# DtoActivityWorkflowData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ConstantActivityType**](ConstantActivityType.md) |  | [optional] 
**created_at** | [**ConvertNullTime**](ConvertNullTime.md) |  | [optional] 
**group** | [**DtoOrganizationUnion**](DtoOrganizationUnion.md) |  | [optional] 
**release** | [**DtoActivityRelease**](DtoActivityRelease.md) |  | [optional] 
**repo** | [**DtoActivityRepos**](DtoActivityRepos.md) |  | [optional] 
**user** | [**DtoActivityUsers**](DtoActivityUsers.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_workflow_data import DtoActivityWorkflowData

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityWorkflowData from a JSON string
dto_activity_workflow_data_instance = DtoActivityWorkflowData.from_json(json)
# print the JSON string representation of the object
print(DtoActivityWorkflowData.to_json())

# convert the object into a dict
dto_activity_workflow_data_dict = dto_activity_workflow_data_instance.to_dict()
# create an instance of DtoActivityWorkflowData from a dict
dto_activity_workflow_data_from_dict = DtoActivityWorkflowData.from_dict(dto_activity_workflow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


