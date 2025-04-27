# DtoActivityMineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | [**ConstantActivityType**](ConstantActivityType.md) |  | [optional] 
**created_at** | [**ConvertNullTime**](ConvertNullTime.md) |  | [optional] 
**repo** | [**DtoActivityRepos**](DtoActivityRepos.md) |  | [optional] 
**user** | [**DtoActivityUsers**](DtoActivityUsers.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_activity_mine_data import DtoActivityMineData

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityMineData from a JSON string
dto_activity_mine_data_instance = DtoActivityMineData.from_json(json)
# print the JSON string representation of the object
print(DtoActivityMineData.to_json())

# convert the object into a dict
dto_activity_mine_data_dict = dto_activity_mine_data_instance.to_dict()
# create an instance of DtoActivityMineData from a dict
dto_activity_mine_data_from_dict = DtoActivityMineData.from_dict(dto_activity_mine_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


