# WebLabelWithCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**issue_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pull_request_count** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_label_with_count import WebLabelWithCount

# TODO update the JSON string below
json = "{}"
# create an instance of WebLabelWithCount from a JSON string
web_label_with_count_instance = WebLabelWithCount.from_json(json)
# print the JSON string representation of the object
print(WebLabelWithCount.to_json())

# convert the object into a dict
web_label_with_count_dict = web_label_with_count_instance.to_dict()
# create an instance of WebLabelWithCount from a dict
web_label_with_count_from_dict = WebLabelWithCount.from_dict(web_label_with_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


