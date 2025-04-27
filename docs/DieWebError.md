# DieWebError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errcode** | **int** |  | [optional] 
**errmsg** | **str** |  | [optional] 
**errparam** | **Dict[str, object]** |  | [optional] 

## Example

```python
from cnb_api.models.die_web_error import DieWebError

# TODO update the JSON string below
json = "{}"
# create an instance of DieWebError from a JSON string
die_web_error_instance = DieWebError.from_json(json)
# print the JSON string representation of the object
print(DieWebError.to_json())

# convert the object into a dict
die_web_error_dict = die_web_error_instance.to_dict()
# create an instance of DieWebError from a dict
die_web_error_from_dict = DieWebError.from_dict(die_web_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


