# ApiPostBlobForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** | 当前编码只支持 &#x60;\&quot;utf-8\&quot;&#x60; and &#x60;\&quot;base64\&quot;&#x60; 。默认: &#x60;utf-8&#x60; | [optional] 

## Example

```python
from cnb_api.models.api_post_blob_form import ApiPostBlobForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPostBlobForm from a JSON string
api_post_blob_form_instance = ApiPostBlobForm.from_json(json)
# print the JSON string representation of the object
print(ApiPostBlobForm.to_json())

# convert the object into a dict
api_post_blob_form_dict = api_post_blob_form_instance.to_dict()
# create an instance of ApiPostBlobForm from a dict
api_post_blob_form_from_dict = ApiPostBlobForm.from_dict(api_post_blob_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


