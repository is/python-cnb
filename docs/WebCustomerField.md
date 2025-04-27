# WebCustomerField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.web_customer_field import WebCustomerField

# TODO update the JSON string below
json = "{}"
# create an instance of WebCustomerField from a JSON string
web_customer_field_instance = WebCustomerField.from_json(json)
# print the JSON string representation of the object
print(WebCustomerField.to_json())

# convert the object into a dict
web_customer_field_dict = web_customer_field_instance.to_dict()
# create an instance of WebCustomerField from a dict
web_customer_field_from_dict = WebCustomerField.from_dict(web_customer_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


