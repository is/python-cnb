# DtoGetMineCreateDetailRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_datas** | [**List[DtoIssueData]**](DtoIssueData.md) |  | [optional] 
**mine_type** | **str** |  | [optional] 
**pull_request_datas** | [**List[DtoPullRequestData]**](DtoPullRequestData.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_get_mine_create_detail_rsp import DtoGetMineCreateDetailRsp

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetMineCreateDetailRsp from a JSON string
dto_get_mine_create_detail_rsp_instance = DtoGetMineCreateDetailRsp.from_json(json)
# print the JSON string representation of the object
print(DtoGetMineCreateDetailRsp.to_json())

# convert the object into a dict
dto_get_mine_create_detail_rsp_dict = dto_get_mine_create_detail_rsp_instance.to_dict()
# create an instance of DtoGetMineCreateDetailRsp from a dict
dto_get_mine_create_detail_rsp_from_dict = DtoGetMineCreateDetailRsp.from_dict(dto_get_mine_create_detail_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


