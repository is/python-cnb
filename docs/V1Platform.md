# V1Platform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Architecture field specifies the CPU architecture, for example &#x60;amd64&#x60; or &#x60;ppc64le&#x60;. | [optional] 
**os** | **str** | OS specifies the operating system, for example &#x60;linux&#x60; or &#x60;windows&#x60;. | [optional] 
**os_features** | **List[str]** | OSFeatures is an optional field specifying an array of strings, each listing a required OS feature (for example on Windows &#x60;win32k&#x60;). | [optional] 
**os_version** | **str** | OSVersion is an optional field specifying the operating system version, for example on Windows &#x60;10.0.14393.1066&#x60;. | [optional] 
**variant** | **str** | Variant is an optional field specifying a variant of the CPU, for example &#x60;v7&#x60; to specify ARMv7 when architecture is &#x60;arm&#x60;. | [optional] 

## Example

```python
from cnb_api.models.v1_platform import V1Platform

# TODO update the JSON string below
json = "{}"
# create an instance of V1Platform from a JSON string
v1_platform_instance = V1Platform.from_json(json)
# print the JSON string representation of the object
print(V1Platform.to_json())

# convert the object into a dict
v1_platform_dict = v1_platform_instance.to_dict()
# create an instance of V1Platform from a dict
v1_platform_from_dict = V1Platform.from_dict(v1_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


