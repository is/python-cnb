# DtoBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type_ci** | **int** | 单位：核时 | [optional] 
**charge_type_ci_policy** | **float** |  | [optional] 
**charge_type_ci_price** | **float** | ci价格，单位：分 | [optional] 
**charge_type_dev** | **int** |  | [optional] 
**charge_type_dev_policy** | **float** |  | [optional] 
**charge_type_dev_price** | **float** | 开发价格，单位：分 | [optional] 
**charge_type_git** | **int** | 单位：Gib | [optional] 
**charge_type_git_policy** | **float** | 折扣，没折扣是100 | [optional] 
**charge_type_git_price** | **float** | git存储价格，单位：分 | [optional] 
**charge_type_object** | **int** |  | [optional] 
**charge_type_object_policy** | **float** |  | [optional] 
**charge_type_object_price** | **float** | 对象存储价格，单位：分 | [optional] 
**name** | **str** | 预算单名称 | [optional] 
**status** | [**ConstantBudgetSts**](ConstantBudgetSts.md) | 预算单状态，1-正常，2-隔离，3-销毁 | [optional] 
**uin** | **str** | 云账号id | [optional] 

## Example

```python
from cnb_api.models.dto_budget import DtoBudget

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBudget from a JSON string
dto_budget_instance = DtoBudget.from_json(json)
# print the JSON string representation of the object
print(DtoBudget.to_json())

# convert the object into a dict
dto_budget_dict = dto_budget_instance.to_dict()
# create an instance of DtoBudget from a dict
dto_budget_from_dict = DtoBudget.from_dict(dto_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


