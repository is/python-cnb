# DtoStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_status** | [**ConstantBudgetSts**](ConstantBudgetSts.md) | 预算单状态，0-没有预算单，1-正常，2-欠费被隔离，3-被销毁 | [optional] 
**threshold** | [**Dict[str, DtoThreshold]**](DtoThreshold.md) | 对应资源类型阈值状态 | [optional] 

## Example

```python
from cnb_api.models.dto_status import DtoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DtoStatus from a JSON string
dto_status_instance = DtoStatus.from_json(json)
# print the JSON string representation of the object
print(DtoStatus.to_json())

# convert the object into a dict
dto_status_dict = dto_status_instance.to_dict()
# create an instance of DtoStatus from a dict
dto_status_from_dict = DtoStatus.from_dict(dto_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


