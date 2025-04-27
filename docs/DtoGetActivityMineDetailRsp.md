# DtoGetActivityMineDetailRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_mine_datas** | [**List[DtoActivityMineData]**](DtoActivityMineData.md) |  | [optional] 
**next_offset** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_get_activity_mine_detail_rsp import DtoGetActivityMineDetailRsp

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetActivityMineDetailRsp from a JSON string
dto_get_activity_mine_detail_rsp_instance = DtoGetActivityMineDetailRsp.from_json(json)
# print the JSON string representation of the object
print(DtoGetActivityMineDetailRsp.to_json())

# convert the object into a dict
dto_get_activity_mine_detail_rsp_dict = dto_get_activity_mine_detail_rsp_instance.to_dict()
# create an instance of DtoGetActivityMineDetailRsp from a dict
dto_get_activity_mine_detail_rsp_from_dict = DtoGetActivityMineDetailRsp.from_dict(dto_get_activity_mine_detail_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


