# ApiPullReviewCommentCreationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**end_line** | **int** |  | [optional] 
**end_side** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**start_line** | **int** |  | [optional] 
**start_side** | **str** |  | [optional] 
**subject_type** | **str** | can be one of: line, file | [optional] 

## Example

```python
from cnb_api.models.api_pull_review_comment_creation_form import ApiPullReviewCommentCreationForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullReviewCommentCreationForm from a JSON string
api_pull_review_comment_creation_form_instance = ApiPullReviewCommentCreationForm.from_json(json)
# print the JSON string representation of the object
print(ApiPullReviewCommentCreationForm.to_json())

# convert the object into a dict
api_pull_review_comment_creation_form_dict = api_pull_review_comment_creation_form_instance.to_dict()
# create an instance of ApiPullReviewCommentCreationForm from a dict
api_pull_review_comment_creation_form_from_dict = ApiPullReviewCommentCreationForm.from_dict(api_pull_review_comment_creation_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


