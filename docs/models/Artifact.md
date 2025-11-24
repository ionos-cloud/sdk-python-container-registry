# Artifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **str** |  | 
**digest** | **str** | The digest of the artifact | 
**tags** | **list[str]** | The tags of an artifact | [optional] 
**media_type** | **str** | The media type of the artifact | 

## Example

```python
from ionoscloud_container_registry.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_from_dict = Artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


