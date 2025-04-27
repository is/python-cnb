# WebMergeState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicts** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_merge_state import WebMergeState

# TODO update the JSON string below
json = "{}"
# create an instance of WebMergeState from a JSON string
web_merge_state_instance = WebMergeState.from_json(json)
# print the JSON string representation of the object
print(WebMergeState.to_json())

# convert the object into a dict
web_merge_state_dict = web_merge_state_instance.to_dict()
# create an instance of WebMergeState from a dict
web_merge_state_from_dict = WebMergeState.from_dict(web_merge_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


