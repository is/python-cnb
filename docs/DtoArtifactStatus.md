# DtoArtifactStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 

## Example

```python
from cnb_api.models.dto_artifact_status import DtoArtifactStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DtoArtifactStatus from a JSON string
dto_artifact_status_instance = DtoArtifactStatus.from_json(json)
# print the JSON string representation of the object
print(DtoArtifactStatus.to_json())

# convert the object into a dict
dto_artifact_status_dict = dto_artifact_status_instance.to_dict()
# create an instance of DtoArtifactStatus from a dict
dto_artifact_status_from_dict = DtoArtifactStatus.from_dict(dto_artifact_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


