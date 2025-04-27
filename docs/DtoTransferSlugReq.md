# DtoTransferSlugReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_transfer_slug_req import DtoTransferSlugReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTransferSlugReq from a JSON string
dto_transfer_slug_req_instance = DtoTransferSlugReq.from_json(json)
# print the JSON string representation of the object
print(DtoTransferSlugReq.to_json())

# convert the object into a dict
dto_transfer_slug_req_dict = dto_transfer_slug_req_instance.to_dict()
# create an instance of DtoTransferSlugReq from a dict
dto_transfer_slug_req_from_dict = DtoTransferSlugReq.from_dict(dto_transfer_slug_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


