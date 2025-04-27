# WebRepoContribTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**WebMeta**](WebMeta.md) |  | [optional] 
**repo_data** | [**List[WebWeek]**](WebWeek.md) |  | [optional] 
**user_total** | **int** |  | [optional] 
**users_data** | [**List[WebContributorTrend]**](WebContributorTrend.md) |  | [optional] 
**week_total** | **int** |  | [optional] 
**with_line_counts** | **bool** | 是否统计增删的行数, 默认总提交超过 10000 的仓库不统计 | [optional] 

## Example

```python
from cnb_api.models.web_repo_contrib_trend import WebRepoContribTrend

# TODO update the JSON string below
json = "{}"
# create an instance of WebRepoContribTrend from a JSON string
web_repo_contrib_trend_instance = WebRepoContribTrend.from_json(json)
# print the JSON string representation of the object
print(WebRepoContribTrend.to_json())

# convert the object into a dict
web_repo_contrib_trend_dict = web_repo_contrib_trend_instance.to_dict()
# create an instance of WebRepoContribTrend from a dict
web_repo_contrib_trend_from_dict = WebRepoContribTrend.from_dict(web_repo_contrib_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


