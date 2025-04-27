# WebapiPullRequestReviewID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_ids** | **List[str]** |  | [optional] 
**review_id** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.webapi_pull_request_review_id import WebapiPullRequestReviewID

# TODO update the JSON string below
json = "{}"
# create an instance of WebapiPullRequestReviewID from a JSON string
webapi_pull_request_review_id_instance = WebapiPullRequestReviewID.from_json(json)
# print the JSON string representation of the object
print(WebapiPullRequestReviewID.to_json())

# convert the object into a dict
webapi_pull_request_review_id_dict = webapi_pull_request_review_id_instance.to_dict()
# create an instance of WebapiPullRequestReviewID from a dict
webapi_pull_request_review_id_from_dict = WebapiPullRequestReviewID.from_dict(webapi_pull_request_review_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


