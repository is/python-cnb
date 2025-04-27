# DtoAssetSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_in_byte** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_asset_size import DtoAssetSize

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAssetSize from a JSON string
dto_asset_size_instance = DtoAssetSize.from_json(json)
# print the JSON string representation of the object
print(DtoAssetSize.to_json())

# convert the object into a dict
dto_asset_size_dict = dto_asset_size_instance.to_dict()
# create an instance of DtoAssetSize from a dict
dto_asset_size_from_dict = DtoAssetSize.from_dict(dto_asset_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


