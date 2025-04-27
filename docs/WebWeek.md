# WebWeek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a** | **int** | 每周增加的行数 | [optional] 
**c** | **int** | 每周的提交数量 | [optional] 
**d** | **int** | 每周删除的行数 | [optional] 
**w** | **int** | 周的时间戳 | [optional] 

## Example

```python
from cnb_api.models.web_week import WebWeek

# TODO update the JSON string below
json = "{}"
# create an instance of WebWeek from a JSON string
web_week_instance = WebWeek.from_json(json)
# print the JSON string representation of the object
print(WebWeek.to_json())

# convert the object into a dict
web_week_dict = web_week_instance.to_dict()
# create an instance of WebWeek from a dict
web_week_from_dict = WebWeek.from_dict(web_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


