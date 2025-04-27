# WebGetCommitAnnotationsInBatchForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_hashes** | **List[str]** |  | [optional] 
**keys** | **List[str]** |  | [optional] 

## Example

```python
from cnb_api.models.web_get_commit_annotations_in_batch_form import WebGetCommitAnnotationsInBatchForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebGetCommitAnnotationsInBatchForm from a JSON string
web_get_commit_annotations_in_batch_form_instance = WebGetCommitAnnotationsInBatchForm.from_json(json)
# print the JSON string representation of the object
print(WebGetCommitAnnotationsInBatchForm.to_json())

# convert the object into a dict
web_get_commit_annotations_in_batch_form_dict = web_get_commit_annotations_in_batch_form_instance.to_dict()
# create an instance of WebGetCommitAnnotationsInBatchForm from a dict
web_get_commit_annotations_in_batch_form_from_dict = WebGetCommitAnnotationsInBatchForm.from_dict(web_get_commit_annotations_in_batch_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


