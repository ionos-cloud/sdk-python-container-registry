# RegistryArtifactsReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**href** | **str** |  | 
**items** | [**list[ArtifactRead]**](ArtifactRead.md) |  | [optional] 
**offset** | **int** | The offset specified in the request (if none was specified, the default offset is 0).  | [readonly] 
**limit** | **int** | The limit specified in the request (if none was specified, use the endpoint&#39;s default pagination limit).  | [readonly] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.registry_artifacts_read_list import RegistryArtifactsReadList

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryArtifactsReadList from a JSON string
registry_artifacts_read_list_instance = RegistryArtifactsReadList.from_json(json)
# print the JSON string representation of the object
print(RegistryArtifactsReadList.to_json())

# convert the object into a dict
registry_artifacts_read_list_dict = registry_artifacts_read_list_instance.to_dict()
# create an instance of RegistryArtifactsReadList from a dict
registry_artifacts_read_list_from_dict = RegistryArtifactsReadList.from_dict(registry_artifacts_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


