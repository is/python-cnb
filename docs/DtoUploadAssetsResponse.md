# DtoUploadAssetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**DtoAssets**](DtoAssets.md) |  | [optional] 
**form** | **Dict[str, str]** |  | [optional] 
**token** | **str** | 后续调用 confirm 接口用的 | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_upload_assets_response import DtoUploadAssetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUploadAssetsResponse from a JSON string
dto_upload_assets_response_instance = DtoUploadAssetsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoUploadAssetsResponse.to_json())

# convert the object into a dict
dto_upload_assets_response_dict = dto_upload_assets_response_instance.to_dict()
# create an instance of DtoUploadAssetsResponse from a dict
dto_upload_assets_response_from_dict = DtoUploadAssetsResponse.from_dict(dto_upload_assets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


