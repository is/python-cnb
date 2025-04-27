# DtoAssets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_assets import DtoAssets

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAssets from a JSON string
dto_assets_instance = DtoAssets.from_json(json)
# print the JSON string representation of the object
print(DtoAssets.to_json())

# convert the object into a dict
dto_assets_dict = dto_assets_instance.to_dict()
# create an instance of DtoAssets from a dict
dto_assets_from_dict = DtoAssets.from_dict(dto_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


