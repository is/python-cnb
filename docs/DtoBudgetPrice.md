# DtoBudgetPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_type_ci_price** | **float** | ci价格，单位：分 | [optional] 
**charge_type_dev_price** | **float** | 开发价格，单位：分 | [optional] 
**charge_type_git_price** | **float** | git存储价格，单位：分 | [optional] 
**charge_type_object_price** | **float** | 对象存储价格，单位：分 | [optional] 

## Example

```python
from cnb_api.models.dto_budget_price import DtoBudgetPrice

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBudgetPrice from a JSON string
dto_budget_price_instance = DtoBudgetPrice.from_json(json)
# print the JSON string representation of the object
print(DtoBudgetPrice.to_json())

# convert the object into a dict
dto_budget_price_dict = dto_budget_price_instance.to_dict()
# create an instance of DtoBudgetPrice from a dict
dto_budget_price_from_dict = DtoBudgetPrice.from_dict(dto_budget_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


