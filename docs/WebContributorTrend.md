# WebContributorTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebAuthor**](WebAuthor.md) | 贡献者信息 | [optional] 
**commit_count** | **int** | 贡献者的总提交数 | [optional] 
**weeks** | [**List[WebWeek]**](WebWeek.md) | 贡献者以周为单位的提交趋势数据 | [optional] 

## Example

```python
from cnb_api.models.web_contributor_trend import WebContributorTrend

# TODO update the JSON string below
json = "{}"
# create an instance of WebContributorTrend from a JSON string
web_contributor_trend_instance = WebContributorTrend.from_json(json)
# print the JSON string representation of the object
print(WebContributorTrend.to_json())

# convert the object into a dict
web_contributor_trend_dict = web_contributor_trend_instance.to_dict()
# create an instance of WebContributorTrend from a dict
web_contributor_trend_from_dict = WebContributorTrend.from_dict(web_contributor_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


