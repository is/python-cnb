# DtoPack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**res_type** | [**ConstantChargeResType**](ConstantChargeResType.md) |  | [optional] 
**size** | **int** | 单位: GiB/核时 | [optional] 
**type** | [**DtoPackType**](DtoPackType.md) |  | [optional] 

## Example

```python
from cnb_api.models.dto_pack import DtoPack

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPack from a JSON string
dto_pack_instance = DtoPack.from_json(json)
# print the JSON string representation of the object
print(DtoPack.to_json())

# convert the object into a dict
dto_pack_dict = dto_pack_instance.to_dict()
# create an instance of DtoPack from a dict
dto_pack_from_dict = DtoPack.from_dict(dto_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


