# WebPullRequestSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_merge_styles** | **List[str]** |  | [optional] 
**base_branch_protection** | [**WebPullRequestBranchProtection**](WebPullRequestBranchProtection.md) |  | [optional] 
**merge_commit_message_style** | **str** |  | [optional] 
**squash_commit_message_style** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_pull_request_setting import WebPullRequestSetting

# TODO update the JSON string below
json = "{}"
# create an instance of WebPullRequestSetting from a JSON string
web_pull_request_setting_instance = WebPullRequestSetting.from_json(json)
# print the JSON string representation of the object
print(WebPullRequestSetting.to_json())

# convert the object into a dict
web_pull_request_setting_dict = web_pull_request_setting_instance.to_dict()
# create an instance of WebPullRequestSetting from a dict
web_pull_request_setting_from_dict = WebPullRequestSetting.from_dict(web_pull_request_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


