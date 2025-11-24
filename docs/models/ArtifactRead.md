# ArtifactRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The digest of the artifact | 
**type** | **str** |  | 
**href** | **str** |  | 
**metadata** | [**ArtifactMetadata**](ArtifactMetadata.md) |  | 
**properties** | [**Artifact**](Artifact.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.artifact_read import ArtifactRead

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRead from a JSON string
artifact_read_instance = ArtifactRead.from_json(json)
# print the JSON string representation of the object
print(ArtifactRead.to_json())

# convert the object into a dict
artifact_read_dict = artifact_read_instance.to_dict()
# create an instance of ArtifactRead from a dict
artifact_read_from_dict = ArtifactRead.from_dict(artifact_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


