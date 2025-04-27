# DtoCreateRepoReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] [default to 'public']

## Example

```python
from cnb_api.models.dto_create_repo_req import DtoCreateRepoReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateRepoReq from a JSON string
dto_create_repo_req_instance = DtoCreateRepoReq.from_json(json)
# print the JSON string representation of the object
print(DtoCreateRepoReq.to_json())

# convert the object into a dict
dto_create_repo_req_dict = dto_create_repo_req_instance.to_dict()
# create an instance of DtoCreateRepoReq from a dict
dto_create_repo_req_from_dict = DtoCreateRepoReq.from_dict(dto_create_repo_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


