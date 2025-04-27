# WebIssueSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_issue_number** | **int** |  | [optional] 
**closed_pull_request_number** | **int** |  | [optional] 
**open_issue_number** | **int** |  | [optional] 
**open_pull_request_number** | **int** |  | [optional] 

## Example

```python
from cnb_api.models.web_issue_summary import WebIssueSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WebIssueSummary from a JSON string
web_issue_summary_instance = WebIssueSummary.from_json(json)
# print the JSON string representation of the object
print(WebIssueSummary.to_json())

# convert the object into a dict
web_issue_summary_dict = web_issue_summary_instance.to_dict()
# create an instance of WebIssueSummary from a dict
web_issue_summary_from_dict = WebIssueSummary.from_dict(web_issue_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


