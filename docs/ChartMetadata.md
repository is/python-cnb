# ChartMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | Annotations are additional mappings uninterpreted by Helm, made available for inspection by other applications. | [optional] 
**api_version** | **str** | The API Version of this chart. Required. | [optional] 
**app_version** | **str** | The version of the application enclosed inside of this chart. | [optional] 
**condition** | **str** | The condition to check to enable chart | [optional] 
**dependencies** | [**List[ChartDependency]**](ChartDependency.md) | Dependencies are a list of dependencies for a chart. | [optional] 
**deprecated** | **bool** | Whether or not this chart is deprecated | [optional] 
**description** | **str** | A one-sentence description of the chart | [optional] 
**home** | **str** | The URL to a relevant project page, git repo, or contact person | [optional] 
**icon** | **str** | The URL to an icon file. | [optional] 
**keywords** | **List[str]** | A list of string keywords | [optional] 
**kube_version** | **str** | KubeVersion is a SemVer constraint specifying the version of Kubernetes required. | [optional] 
**maintainers** | [**List[ChartMaintainer]**](ChartMaintainer.md) | A list of name and URL/email address combinations for the maintainer(s) | [optional] 
**name** | **str** | The name of the chart. Required. | [optional] 
**sources** | **List[str]** | Source is the URL to the source code of this chart | [optional] 
**tags** | **str** | The tags to check to enable chart | [optional] 
**type** | **str** | Specifies the chart type: application or library | [optional] 
**version** | **str** | A SemVer 2 conformant version string of the chart. Required. | [optional] 

## Example

```python
from cnb_api.models.chart_metadata import ChartMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ChartMetadata from a JSON string
chart_metadata_instance = ChartMetadata.from_json(json)
# print the JSON string representation of the object
print(ChartMetadata.to_json())

# convert the object into a dict
chart_metadata_dict = chart_metadata_instance.to_dict()
# create an instance of ChartMetadata from a dict
chart_metadata_from_dict = ChartMetadata.from_dict(chart_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


