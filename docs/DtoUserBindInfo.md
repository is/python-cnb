# DtoUserBindInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**expire_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nick** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_user_bind_info import DtoUserBindInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserBindInfo from a JSON string
dto_user_bind_info_instance = DtoUserBindInfo.from_json(json)
# print the JSON string representation of the object
print(DtoUserBindInfo.to_json())

# convert the object into a dict
dto_user_bind_info_dict = dto_user_bind_info_instance.to_dict()
# create an instance of DtoUserBindInfo from a dict
dto_user_bind_info_from_dict = DtoUserBindInfo.from_dict(dto_user_bind_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


