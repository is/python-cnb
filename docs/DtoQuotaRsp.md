# DtoQuotaRsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | [**DtoStorage**](DtoStorage.md) | The hard limits of the quota,example: { \&quot;hard\&quot;: { \&quot;storage\&quot;: -1}} | [optional] 
**repository_name** | **str** | The repository name of the quota | [optional] 
**storage_per_project** | **str** | The cnb default quota value | [optional] 
**used** | [**DtoStorage**](DtoStorage.md) | The used limits of the quota,example: { \&quot;used\&quot;: { \&quot;storage\&quot;: 0}} | [optional] 

## Example

```python
from cnb_api.models.dto_quota_rsp import DtoQuotaRsp

# TODO update the JSON string below
json = "{}"
# create an instance of DtoQuotaRsp from a JSON string
dto_quota_rsp_instance = DtoQuotaRsp.from_json(json)
# print the JSON string representation of the object
print(DtoQuotaRsp.to_json())

# convert the object into a dict
dto_quota_rsp_dict = dto_quota_rsp_instance.to_dict()
# create an instance of DtoQuotaRsp from a dict
dto_quota_rsp_from_dict = DtoQuotaRsp.from_dict(dto_quota_rsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


