# DieWebErr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errcode** | **int** |  | [optional] 
**errmsg** | **str** |  | [optional] 
**errparam** | **Dict[str, object]** |  | [optional] 

## Example

```python
from cnb_api.models.die_web_err import DieWebErr

# TODO update the JSON string below
json = "{}"
# create an instance of DieWebErr from a JSON string
die_web_err_instance = DieWebErr.from_json(json)
# print the JSON string representation of the object
print(DieWebErr.to_json())

# convert the object into a dict
die_web_err_dict = die_web_err_instance.to_dict()
# create an instance of DieWebErr from a dict
die_web_err_from_dict = DieWebErr.from_dict(die_web_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


