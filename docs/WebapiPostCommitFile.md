# WebapiPostCommitFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_executable** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_commit_file import WebapiPostCommitFile

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostCommitFile from a JSON string
webapi_post_commit_file_instance = WebapiPostCommitFile.from_json(json)
# print the JSON string representation of the object
print(WebapiPostCommitFile.to_json())

# convert the object into a dict
webapi_post_commit_file_dict = webapi_post_commit_file_instance.to_dict()
# create an instance of WebapiPostCommitFile from a dict
webapi_post_commit_file_from_dict = WebapiPostCommitFile.from_dict(webapi_post_commit_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


