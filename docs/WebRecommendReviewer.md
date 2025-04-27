# WebRecommendReviewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_recommend_reviewer import WebRecommendReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of WebRecommendReviewer from a JSON string
web_recommend_reviewer_instance = WebRecommendReviewer.from_json(json)
# print the JSON string representation of the object
print(WebRecommendReviewer.to_json())

# convert the object into a dict
web_recommend_reviewer_dict = web_recommend_reviewer_instance.to_dict()
# create an instance of WebRecommendReviewer from a dict
web_recommend_reviewer_from_dict = WebRecommendReviewer.from_dict(web_recommend_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


