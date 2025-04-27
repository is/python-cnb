# WebDiffStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletions** | **int** |  | [optional] 
**entry_exceeded** | **bool** |  | [optional] 
**entry_limit** | **int** |  | [optional] 
**insertions** | **int** |  | [optional] 
**paths** | [**List[WebDiffEntry]**](WebDiffEntry.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_diff_stat import WebDiffStat

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiffStat from a JSON string
web_diff_stat_instance = WebDiffStat.from_json(json)
# print the JSON string representation of the object
print(WebDiffStat.to_json())

# convert the object into a dict
web_diff_stat_dict = web_diff_stat_instance.to_dict()
# create an instance of WebDiffStat from a dict
web_diff_stat_from_dict = WebDiffStat.from_dict(web_diff_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


