# ApiBlob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_blob import ApiBlob

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBlob from a JSON string
api_blob_instance = ApiBlob.from_json(json)
# print the JSON string representation of the object
print(ApiBlob.to_json())

# convert the object into a dict
api_blob_dict = api_blob_instance.to_dict()
# create an instance of ApiBlob from a dict
api_blob_from_dict = ApiBlob.from_dict(api_blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


