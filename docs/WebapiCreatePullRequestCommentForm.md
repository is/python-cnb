# WebapiCreatePullRequestCommentForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_create_pull_request_comment_form import WebapiCreatePullRequestCommentForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiCreatePullRequestCommentForm from a JSON string
webapi_create_pull_request_comment_form_instance = WebapiCreatePullRequestCommentForm.from_json(json)
# print the JSON string representation of the object
print(WebapiCreatePullRequestCommentForm.to_json())

# convert the object into a dict
webapi_create_pull_request_comment_form_dict = webapi_create_pull_request_comment_form_instance.to_dict()
# create an instance of WebapiCreatePullRequestCommentForm from a dict
webapi_create_pull_request_comment_form_from_dict = WebapiCreatePullRequestCommentForm.from_dict(webapi_create_pull_request_comment_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


