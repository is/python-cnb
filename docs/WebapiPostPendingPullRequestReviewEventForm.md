# WebapiPostPendingPullRequestReviewEventForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**event** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_post_pending_pull_request_review_event_form import WebapiPostPendingPullRequestReviewEventForm

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPostPendingPullRequestReviewEventForm from a JSON string
webapi_post_pending_pull_request_review_event_form_instance = WebapiPostPendingPullRequestReviewEventForm.from_json(json)
# print the JSON string representation of the object
print(WebapiPostPendingPullRequestReviewEventForm.to_json())

# convert the object into a dict
webapi_post_pending_pull_request_review_event_form_dict = webapi_post_pending_pull_request_review_event_form_instance.to_dict()
# create an instance of WebapiPostPendingPullRequestReviewEventForm from a dict
webapi_post_pending_pull_request_review_event_form_from_dict = WebapiPostPendingPullRequestReviewEventForm.from_dict(webapi_post_pending_pull_request_review_event_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


