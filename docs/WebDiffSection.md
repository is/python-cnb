# WebDiffSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[WebDiffLine]**](WebDiffLine.md) |  | [optional] 

## Example

```python
from cnb_api.models.web_diff_section import WebDiffSection

# TODO update the JSON string below
json = "{}"
# create an instance of WebDiffSection from a JSON string
web_diff_section_instance = WebDiffSection.from_json(json)
# print the JSON string representation of the object
print(WebDiffSection.to_json())

# convert the object into a dict
web_diff_section_dict = web_diff_section_instance.to_dict()
# create an instance of WebDiffSection from a dict
web_diff_section_from_dict = WebDiffSection.from_dict(web_diff_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


