# DtoCheckFollowingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_following** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.dto_check_following_response import DtoCheckFollowingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCheckFollowingResponse from a JSON string
dto_check_following_response_instance = DtoCheckFollowingResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCheckFollowingResponse.to_json())

# convert the object into a dict
dto_check_following_response_dict = dto_check_following_response_instance.to_dict()
# create an instance of DtoCheckFollowingResponse from a dict
dto_check_following_response_from_dict = DtoCheckFollowingResponse.from_dict(dto_check_following_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


