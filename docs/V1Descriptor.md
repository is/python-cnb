# V1Descriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | Annotations contains arbitrary metadata relating to the targeted content. | [optional] 
**artifact_type** | **str** | ArtifactType is the IANA media type of this artifact. | [optional] 
**data** | **List[int]** | Data is an embedding of the targeted content. This is encoded as a base64 string when marshalled to JSON (automatically, by encoding/json). If present, Data can be used directly to avoid fetching the targeted content. | [optional] 
**digest** | **str** | Digest is the digest of the targeted content. | [optional] 
**media_type** | **str** | MediaType is the media type of the object this schema refers to. | [optional] 
**platform** | [**V1Platform**](V1Platform.md) | Platform describes the platform which the image in the manifest runs on.  This should only be used when referring to a manifest. | [optional] 
**size** | **int** | Size specifies the size in bytes of the blob. | [optional] 
**urls** | **List[str]** | URLs specifies a list of URLs from which this object MAY be downloaded | [optional] 

## Example

```python
from cnb_api.models.v1_descriptor import V1Descriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V1Descriptor from a JSON string
v1_descriptor_instance = V1Descriptor.from_json(json)
# print the JSON string representation of the object
print(V1Descriptor.to_json())

# convert the object into a dict
v1_descriptor_dict = v1_descriptor_instance.to_dict()
# create an instance of V1Descriptor from a dict
v1_descriptor_from_dict = V1Descriptor.from_dict(v1_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


