# ConvertNullTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**valid** | **bool** | Valid is true if Time is not NULL | [optional] 

## Example

```python
from cnb_api.models.convert_null_time import ConvertNullTime

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertNullTime from a JSON string
convert_null_time_instance = ConvertNullTime.from_json(json)
# print the JSON string representation of the object
print(ConvertNullTime.to_json())

# convert the object into a dict
convert_null_time_dict = convert_null_time_instance.to_dict()
# create an instance of ConvertNullTime from a dict
convert_null_time_from_dict = ConvertNullTime.from_dict(convert_null_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


