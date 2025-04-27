# ApiPullReviewCreationForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**comments** | [**List[ApiPullReviewCommentCreationForm]**](ApiPullReviewCommentCreationForm.md) |  | [optional] 
**event** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.api_pull_review_creation_form import ApiPullReviewCreationForm

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullReviewCreationForm from a JSON string
api_pull_review_creation_form_instance = ApiPullReviewCreationForm.from_json(json)
# print the JSON string representation of the object
print(ApiPullReviewCreationForm.to_json())

# convert the object into a dict
api_pull_review_creation_form_dict = api_pull_review_creation_form_instance.to_dict()
# create an instance of ApiPullReviewCreationForm from a dict
api_pull_review_creation_form_from_dict = ApiPullReviewCreationForm.from_dict(api_pull_review_creation_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


