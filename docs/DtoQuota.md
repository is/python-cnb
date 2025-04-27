# DtoQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | [**DtoStorage**](DtoStorage.md) | The hard limits of the quota,example: { \&quot;hard\&quot;: { \&quot;storage\&quot;: -1}} | [optional] 

## Example

```python
from cnb_api.models.dto_quota import DtoQuota

# TODO update the JSON string below
json = "{}"
# create an instance of DtoQuota from a JSON string
dto_quota_instance = DtoQuota.from_json(json)
# print the JSON string representation of the object
print(DtoQuota.to_json())

# convert the object into a dict
dto_quota_dict = dto_quota_instance.to_dict()
# create an instance of DtoQuota from a dict
dto_quota_from_dict = DtoQuota.from_dict(dto_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


