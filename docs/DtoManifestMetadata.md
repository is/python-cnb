# DtoManifestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | Annotations contains arbitrary metadata for the image manifest. | [optional] 
**artifact_type** | **str** | ArtifactType specifies the IANA media type of artifact when the manifest is used for an artifact. | [optional] 
**config** | [**V1Descriptor**](V1Descriptor.md) | Config references a configuration object for a container, by digest. The referenced configuration object is a JSON blob that the runtime uses to set up the container. | [optional] 
**layers** | [**List[V1Descriptor]**](V1Descriptor.md) | Layers is an indexed list of layers referenced by the manifest. | [optional] 
**manifests** | [**List[V1Descriptor]**](V1Descriptor.md) | Manifests references platform specific manifests. | [optional] 
**media_type** | **str** | MediaType specifies the type of this document data structure e.g. &#x60;application/vnd.oci.image.manifest.v1+json&#x60; | [optional] 
**schema_version** | **int** | SchemaVersion is the image manifest schema that this image follows | [optional] 
**subject** | [**V1Descriptor**](V1Descriptor.md) | Subject is an optional link from the image manifest to another manifest forming an association between the image manifest and the other manifest. | [optional] 

## Example

```python
from cnb_api.models.dto_manifest_metadata import DtoManifestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DtoManifestMetadata from a JSON string
dto_manifest_metadata_instance = DtoManifestMetadata.from_json(json)
# print the JSON string representation of the object
print(DtoManifestMetadata.to_json())

# convert the object into a dict
dto_manifest_metadata_dict = dto_manifest_metadata_instance.to_dict()
# create an instance of DtoManifestMetadata from a dict
dto_manifest_metadata_from_dict = DtoManifestMetadata.from_dict(dto_manifest_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


