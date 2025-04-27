# DtoAssetRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**origin_path** | **str** | 来源地址，例如 release 附件的来源地址是对应的 release 页面。issue和pr文件没有。 | [optional] 
**path** | **str** |  | [optional] 
**referer** | **str** |  | [optional] 
**size_in_byte** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_asset_records import DtoAssetRecords

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAssetRecords from a JSON string
dto_asset_records_instance = DtoAssetRecords.from_json(json)
# print the JSON string representation of the object
print(DtoAssetRecords.to_json())

# convert the object into a dict
dto_asset_records_dict = dto_asset_records_instance.to_dict()
# create an instance of DtoAssetRecords from a dict
dto_asset_records_from_dict = DtoAssetRecords.from_dict(dto_asset_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


