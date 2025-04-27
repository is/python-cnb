# DtoCopyReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] [default to 'public']

## Example

```python
from cnb_api.models.dto_copy_req import DtoCopyReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCopyReq from a JSON string
dto_copy_req_instance = DtoCopyReq.from_json(json)
# print the JSON string representation of the object
print(DtoCopyReq.to_json())

# convert the object into a dict
dto_copy_req_dict = dto_copy_req_instance.to_dict()
# create an instance of DtoCopyReq from a dict
dto_copy_req_from_dict = DtoCopyReq.from_dict(dto_copy_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


