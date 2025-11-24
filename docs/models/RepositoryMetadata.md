# RepositoryMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional] [readonly] 
**created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly] 
**created_by_user_id** | **str** | Unique id of the identity that created the resource. | [optional] [readonly] 
**last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional] [readonly] 
**last_modified_by** | **str** | Unique name of the identity that last modified the resource. | [optional] [readonly] 
**last_modified_by_user_id** | **str** | Unique id of the identity that last modified the resource. | [optional] [readonly] 
**resource_urn** | **str** | Unique name of the resource. | [optional] [readonly] 
**artifact_count** | **int** |  | 
**pull_count** | **int** |  | 
**push_count** | **int** |  | 
**last_pulled_at** | **datetime** |  | [optional] 
**last_pushed_at** | **datetime** |  | [optional] 
**last_severity** | **str** | The maximum vulnerability severity of the artifact last pushed in the repository, if any | [optional] 

## Example

```python
from ionoscloud_container_registry.models.repository_metadata import RepositoryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryMetadata from a JSON string
repository_metadata_instance = RepositoryMetadata.from_json(json)
# print the JSON string representation of the object
print(RepositoryMetadata.to_json())

# convert the object into a dict
repository_metadata_dict = repository_metadata_instance.to_dict()
# create an instance of RepositoryMetadata from a dict
repository_metadata_from_dict = RepositoryMetadata.from_dict(repository_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


