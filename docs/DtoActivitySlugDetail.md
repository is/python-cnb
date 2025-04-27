# DtoActivitySlugDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | 完整仓库路径 | [optional] 

## Example

```python
from cnb_api.models.dto_activity_slug_detail import DtoActivitySlugDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivitySlugDetail from a JSON string
dto_activity_slug_detail_instance = DtoActivitySlugDetail.from_json(json)
# print the JSON string representation of the object
print(DtoActivitySlugDetail.to_json())

# convert the object into a dict
dto_activity_slug_detail_dict = dto_activity_slug_detail_instance.to_dict()
# create an instance of DtoActivitySlugDetail from a dict
dto_activity_slug_detail_from_dict = DtoActivitySlugDetail.from_dict(dto_activity_slug_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


