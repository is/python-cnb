# DtoUploadRequestParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.dto_upload_request_params import DtoUploadRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUploadRequestParams from a JSON string
dto_upload_request_params_instance = DtoUploadRequestParams.from_json(json)
# print the JSON string representation of the object
print(DtoUploadRequestParams.to_json())

# convert the object into a dict
dto_upload_request_params_dict = dto_upload_request_params_instance.to_dict()
# create an instance of DtoUploadRequestParams from a dict
dto_upload_request_params_from_dict = DtoUploadRequestParams.from_dict(dto_upload_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


