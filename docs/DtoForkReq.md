# DtoForkReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_fork_req import DtoForkReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoForkReq from a JSON string
dto_fork_req_instance = DtoForkReq.from_json(json)
# print the JSON string representation of the object
print(DtoForkReq.to_json())

# convert the object into a dict
dto_fork_req_dict = dto_fork_req_instance.to_dict()
# create an instance of DtoForkReq from a dict
dto_fork_req_from_dict = DtoForkReq.from_dict(dto_fork_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


