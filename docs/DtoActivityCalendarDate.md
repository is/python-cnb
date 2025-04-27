# DtoActivityCalendarDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_count** | **int** |  | [optional] 
**issues_count** | **int** |  | [optional] 
**pr_count** | **int** |  | [optional] 
**score** | **float** |  | [optional] 
**valid_cr_count** | **int** | 有效cr数，代码评审通过且对应的pr被合入 | [optional] 
**valid_pr_count** | **int** | 有效pr数，已被合入，且pr具有至少一个已通过的代码评审 | [optional] 

## Example

```python
from cnb_api.models.dto_activity_calendar_date import DtoActivityCalendarDate

# TODO update the JSON string below
json = "{}"
# create an instance of DtoActivityCalendarDate from a JSON string
dto_activity_calendar_date_instance = DtoActivityCalendarDate.from_json(json)
# print the JSON string representation of the object
print(DtoActivityCalendarDate.to_json())

# convert the object into a dict
dto_activity_calendar_date_dict = dto_activity_calendar_date_instance.to_dict()
# create an instance of DtoActivityCalendarDate from a dict
dto_activity_calendar_date_from_dict = DtoActivityCalendarDate.from_dict(dto_activity_calendar_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


