# DtoSlugMemberCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inherited_member_count** | **int** | 继承成员总数 | [optional] 
**member_count** | **int** | 直接成员总数 | [optional] 
**outside_collaborator_count** | **int** | 外部协作者总数 | [optional] 

## Example

```python
from cnb_api.models.dto_slug_member_count import DtoSlugMemberCount

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSlugMemberCount from a JSON string
dto_slug_member_count_instance = DtoSlugMemberCount.from_json(json)
# print the JSON string representation of the object
print(DtoSlugMemberCount.to_json())

# convert the object into a dict
dto_slug_member_count_dict = dto_slug_member_count_instance.to_dict()
# create an instance of DtoSlugMemberCount from a dict
dto_slug_member_count_from_dict = DtoSlugMemberCount.from_dict(dto_slug_member_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


