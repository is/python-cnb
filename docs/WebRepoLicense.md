# WebRepoLicense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**license** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_repo_license import WebRepoLicense

# TODO update the JSON string below
json = "{}"
# create an instance of WebRepoLicense from a JSON string
web_repo_license_instance = WebRepoLicense.from_json(json)
# print the JSON string representation of the object
print(WebRepoLicense.to_json())

# convert the object into a dict
web_repo_license_dict = web_repo_license_instance.to_dict()
# create an instance of WebRepoLicense from a dict
web_repo_license_from_dict = WebRepoLicense.from_dict(web_repo_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


