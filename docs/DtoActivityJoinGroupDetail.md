# DtoActivityJoinGroupDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_at** | **str** |  | [optional] 
**detail** | [**DtoOrganizationUnion**](DtoOrganizationUnion.md) | 组织详情，组织被删后为 null | [optional] 
**remark** | **str** | 组织别名，组织被删除后才有值 | [optional] 

## Example

```python
from cnb_api.models.dto_activity_join_group_detail import DtoActivityJoinGroupDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityJoinGroupDetail from a JSON string
dto_activity_join_group_detail_instance = DtoActivityJoinGroupDetail.from_json(json)
# print the JSON string representation of the object
print(DtoActivityJoinGroupDetail.to_json())

# convert the object into a dict
dto_activity_join_group_detail_dict = dto_activity_join_group_detail_instance.to_dict()
# create an instance of DtoActivityJoinGroupDetail from a dict
dto_activity_join_group_detail_from_dict = DtoActivityJoinGroupDetail.from_dict(dto_activity_join_group_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


