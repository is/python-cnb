# DtoRepoLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**language** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_repo_language import DtoRepoLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoRepoLanguage from a JSON string
dto_repo_language_instance = DtoRepoLanguage.from_json(json)
# print the JSON string representation of the object
print(DtoRepoLanguage.to_json())

# convert the object into a dict
dto_repo_language_dict = dto_repo_language_instance.to_dict()
# create an instance of DtoRepoLanguage from a dict
dto_repo_language_from_dict = DtoRepoLanguage.from_dict(dto_repo_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


